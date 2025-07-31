from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import *
from ..Slice import *
from ..SubjectSlice import *

class ClassificationPredictionTask(Task):
   
    def __init__(self,   dataset= None ):
        self.taskType = TaskType( idTaskType = 2,type = 'Prediction')
        self.name = type(self).__name__
        self.dataset = dataset
        self.measureProcedures = [F1MeasureProcedure(),AccuracyMeasureProcedure(),RecallMeasureProcedure(),PrecisionMeasureProcedure(),\
                                  LogLossMeasureProcedure(), FPRMeasureProcedure(), SelectionRateMeasureProcedure()]
        self.measureProceduresProba = [ROCAUCMeasureProcedure(), BrierScoreMeasureProcedure()]


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

        for slice in slices:

            slice_obj = None
            if slice is None:
                df_iter =df 
                X_iter = X
            else:
                description = None 
                if 'description' in slice.keys():
                    description = slice['description']
                condition = slice['condition']

                df_iter = df.query(condition)
                X_iter = X.query(condition) 
                slice_obj = Slice(description= description, condition =condition)
            
            y_pred_iter = df_iter['y_pred']
            y_truth_iter = df_iter[self.target_feature_name]

            for measureProcedure in self.measureProcedures:
                measureValue = measureProcedure.evaluate(y_truth = y_truth_iter, y_pred = y_pred_iter)
                if slice_obj is not None:
                    measureValue.measure.subjectSlices = [SubjectSlice(slice=slice_obj)]

                measureValues.append(measureValue)
           
            y_pred_proba = model.predict_proba(X_iter)
            for measureProcedure in self.measureProceduresProba:
                measureValue = measureProcedure.evaluate(y_truth = y_truth_iter, y_pred_proba = y_pred_proba)
                if slice_obj is not None:
                    measureValue.measure.subjectSlices = [SubjectSlice(slice=slice_obj)]
                measureValues.append(measureValue)
 

        return predictions, measureValues
    
    