from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import RMSEMeasureProcedure
from ..Prediction import *
from tqdm.notebook import tqdm

class SeoulBikePredictionTask(Task):

   
    def __init__(self,   dataset= None):
        self.taskType = TaskType( idTaskType = 2,type = 'Prediction')
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

        df_vars = df.drop(columns = ['timestamp'], errors = 'ignore')

        y = df_vars[targetFeature]
        X = df_vars.drop(columns=[targetFeature])

        y_pred = model.predict(X)
        df['value'] = y_pred
        df['type'] = 'float'

        predictions = df.apply(lambda x : Prediction(**x), axis = 1).to_list()
 

        return predictions, None
    
    