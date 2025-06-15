from ..Task import *
from ..TaskType import * 
from sklearn.model_selection import train_test_split
from ..MeasureProcedures import *

class ClassificationTrainingTask(Task):

   
    def __init__(self,   dataset= None):
        self.taskType = TaskType( idTaskType = 1,type = 'Training')
        self.name = type(self).__name__
        self.dataset = dataset
        self.measureProcedures = [F1MeasureProcedure(),AccuracyMeasureProcedure(),PrecisionMeasureProcedure(),LogLossMeasureProcedure()]

    def execute(self, model, parameters):

        df = self.dataset.df 

        if type(parameters) == dict:
            if 'end_date' in parameters.keys():
                df = df[df['timestamp']<parameters['end_date']].reset_index(drop = True)

        df = df.drop(columns = ['timestamp'], errors = 'ignore')

        y = df[self.target_feature_name]
        X = df.drop(columns=[self.target_feature_name])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model.fit(X_train, y_train)
        predictions = model.predict(X_test, generate_explanations = False)
        y_pred = [p.value for p in predictions]
        measureValues = []
        for measureProcedure in self.measureProcedures:
            measureValue = measureProcedure.evaluate(y_truth = y_test, y_pred = y_pred)
            measureValues.append(measureValue)

        measureProcedure = ROCAUCMeasureProcedure()
        y_pred_proba = model.predict_proba(X_test)
        measureValue = measureProcedure.evaluate(y_truth = y_test, y_pred_proba = y_pred_proba)
        measureValues.append(measureValue)


        return None, measureValues
    
    