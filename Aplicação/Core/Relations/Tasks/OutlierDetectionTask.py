from ..Task import *
from ..TaskType import * 
from ..MeasureProcedures import IsolationForestEvaluationProcedure

import pandas as pd

class OutlierDetectionTask(Task):

   
    def __init__(self):
        self.taskType = TaskType(type = 'Others')
        self.name = type(self).__name__

    def execute(self,  parameters= {}):

        df = self.dataset.df.drop(columns = [self.target_feature_name], errors='ignore') 
         
        if not(isinstance(parameters,dict)):
            return
    
        df_reference = df[df['timestamp']<pd.Timestamp(parameters['end_reference_date'])].drop(columns = ['timestamp'], errors='ignore')
        df_current = df[(df['timestamp']>=pd.Timestamp(parameters['start_current_date'])) & (df['timestamp']<=pd.Timestamp(parameters['end_current_date']))]

        procedure = IsolationForestEvaluationProcedure()
        measureValues = procedure.evaluate(df_reference = df_reference, df_current = df_current)

        return None, measureValues
    
    