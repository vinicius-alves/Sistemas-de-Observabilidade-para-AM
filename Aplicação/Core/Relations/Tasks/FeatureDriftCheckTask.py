from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import JSMeasureProcedure

import pandas as pd

class FeatureDriftCheckTask(Task):

   
    def __init__(self,   dataset= None):
        self.taskType = TaskType(type = 'Others')
        self.name = type(self).__name__
        self.dataset = dataset

    def execute(self, model=None, parameters= {}):

        df = self.dataset.df.drop(columns = ['idEntity'], errors='ignore') 
        name_space_obj = self.dataset.features[0].nameSpace
        name_space_map = {}
        for feature in self.dataset.features:
            name_space_map[feature.name] = feature.nameSpace
        
        if not(isinstance(parameters,dict)):
            return
    
        df_reference = df[df['timestamp']<pd.Timestamp(parameters['end_reference_date'])].drop(columns = ['timestamp'], errors='ignore')
        df_current = df[(df['timestamp']>=pd.Timestamp(parameters['start_current_date'])) & (df['timestamp']<=pd.Timestamp(parameters['end_current_date']))].drop(columns = ['timestamp'], errors='ignore')

        procedure = JSMeasureProcedure()
        measureValues = procedure.evaluate(df_reference = df_reference, df_current = df_current, name_space_map = name_space_map)

        return None, measureValues
    
    