from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import *
from ..Slice import *
from ..SubjectSlice import *

class RegressionPredictionTask(Task):
   
    def __init__(self,   dataset= None ):
        self.taskType = TaskType( idTaskType = 2,type = 'Prediction')
        self.name = type(self).__name__
        self.dataset = dataset
        self.measureProcedures = [RMSEMeasureProcedure(),MAEMeasureProcedure(),R2MeasureProcedure(),MeanErrorMeasureProcedure()]


    def execute(self, model, parameters):

        df = self.dataset.df

        if type(parameters) == dict:
            if 'end_date' in parameters.keys():
                df = df[df['timestamp']<parameters['end_date']].reset_index(drop = True)
            if 'start_date' in parameters.keys():
                df = df[df['timestamp']>=parameters['start_date']].reset_index(drop = True)
        
        X = df.drop(columns=[self.target_feature_name])
        predictions = model.predict(X, generate_explanations = True)

        y_pred = [p.value for p in predictions]
        df['y_pred'] = y_pred 

        measureValues = []
        slices = [None]
        if 'slices' in parameters.keys():
            slices += parameters['slices']

        lst_arrays_pred_slices = []
        for slice in slices:

            slice_obj = None
            if slice is None:
                df_iter =df  
            else:
                description = None 
                if 'description' in slice.keys():
                    description = slice['description']
                condition = slice['condition']

                df_iter = df.query(condition)
                slice_obj = Slice(description= description, condition =condition)

            y_pred_iter = df_iter['y_pred']
            y_truth_iter = df_iter[self.target_feature_name]

            if slice is not None:
                lst_arrays_pred_slices.append( y_pred_iter- y_truth_iter)

            for measureProcedure in self.measureProcedures:
                measureValue = measureProcedure.evaluate(y_truth = y_truth_iter, y_pred = y_pred_iter)
                if slice_obj is not None:
                    measureValue.measure.subjectSlices = [SubjectSlice(slice=slice_obj)]
                measureValues.append(measureValue)

        if len(lst_arrays_pred_slices)>1:
            measureProcedure = KruskalWallisMeasureProcedure()
            measureValue = measureProcedure.evaluate(lst_arrays = lst_arrays_pred_slices)
            measureValues.append(measureValue)

        return predictions, measureValues
    
    