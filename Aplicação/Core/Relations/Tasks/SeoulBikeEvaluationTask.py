from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import RMSEMeasureProcedure

class SeoulBikeEvaluationTask(Task):

   
    def __init__(self,   dataset= None):
        self.taskType = TaskType( idTaskType = 2,type = 'Evaluation')
        self.name = type(self).__name__
        self.dataset = dataset
        measureProcedure = RMSEMeasureProcedure()
        self.measureProcedures = [measureProcedure]


    def execute(self, model, parameters):

        df = self.dataset.df
        targetFeature = self.dataset.targetFeature  

        if type(parameters) == dict:
            if 'end_date' in parameters.keys():
                df = df[df['timestamp']<parameters['end_date']].reset_index(drop = True)
            if 'start_date' in parameters.keys():
                df = df[df['timestamp']>=parameters['start_date']].reset_index(drop = True)

        df = df.drop(columns = ['timestamp'], errors = 'ignore')

        y = df[targetFeature]
        X = df.drop(columns=[targetFeature])

        y_pred = model.predict(X)
        measures = []
        for measureProcedure in self.measureProcedures:
            measure = measureProcedure.evaluate(y_truth = y, y_pred = y_pred)
            measures.append(measure)

        return None, measures
    
    