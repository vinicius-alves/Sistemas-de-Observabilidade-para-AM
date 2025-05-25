from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import *

class SeoulBikePredictionTask(Task):
   
    def __init__(self,   dataset= None ):
        self.taskType = TaskType( idTaskType = 2,type = 'Prediction')
        self.name = type(self).__name__
        self.dataset = dataset
        self.measureProcedures = [RMSEMeasureProcedure(),MAEMeasureProcedure(),R2MeasureProcedure()]


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

        y_truth = df[self.target_feature_name]
        measures = []
        for measureProcedure in self.measureProcedures:
            measure = measureProcedure.evaluate(y_truth = y_truth, y_pred = y_pred)
            measures.append(measure)
 

        return predictions, measures
    
    