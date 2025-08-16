from ..Task import *
from ..TaskType import * 
from sklearn.model_selection import train_test_split
from ..MeasureProcedures import *

class RegressionTrainingTask(Task):

   
    def __init__(self):
        self.taskType = TaskType( idTaskType = 1,type = 'Training')
        self.name = type(self).__name__
        self.measureProcedures = [RMSEMeasureProcedure(),MAEMeasureProcedure(),R2MeasureProcedure(),MeanErrorMeasureProcedure()]

    def execute(self, parameters):

        df = self.dataset.df 

        if type(parameters) == dict:
            if 'end_date' in parameters.keys():
                df = df[df['timestamp']<parameters['end_date']].reset_index(drop = True)

        df = df.drop(columns = ['timestamp'], errors = 'ignore')

        y = df[self.target_feature_name]
        X = df.drop(columns=[self.target_feature_name])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test, generate_explanations = False)
        y_pred = [p.value for p in predictions]
        measureValues = []
        for measureProcedure in self.measureProcedures:
            measureValue = measureProcedure.evaluate(y_truth = y_test, y_pred = y_pred)
            measureValues.append(measureValue)

        return None, measureValues
    
    