from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import RMSEMeasureProcedure

class SeoulBikePredictionTask(Task):

   
    def __init__(self,   dataset= None):
        self.taskType = TaskType( idTaskType = 2,type = 'Regression')
        self.name = type(self).__name__
        self.dataset = dataset
        measureProcedure = RMSEMeasureProcedure()
        self.measureProcedures = [measureProcedure]


    def execute(self, model, parameters):

        df = self.dataset.df
        targetFeature = self.dataset.targetFeature  

        if type(parameters) == dict:
            if 'end_date' in parameters.keys():
                df = df[df['date']<parameters['end_date']].reset_index(drop = True)
            if 'start_date' in parameters.keys():
                df = df[df['date']>=parameters['start_date']].reset_index(drop = True)

        df = df.drop(columns = ['date'], errors = 'ignore')

        y = df[targetFeature]
        X = df.drop(columns=[targetFeature])

        y_pred = model.predict(X)
        measures = []
        for measureProcedure in self.measureProcedures:
            measure = measureProcedure.evaluate(y_truth = y, y_pred = y_pred)
            measures.append(measure)

        return measures
    
    