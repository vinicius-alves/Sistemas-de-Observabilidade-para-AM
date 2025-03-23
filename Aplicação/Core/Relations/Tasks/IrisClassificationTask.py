from ..Task import *
from sklearn.model_selection import train_test_split

class IrisClassificationTask(Task):

   
    def __init__(self,  tastype= None, dataset= None):
        self.tastype = tastype
        self.name = 'IrisClassificationTask'
        self.dataset = dataset


    def execute(self, model, taskParameters, measureProcedures):

        if taskParameters is not None:
            if len(taskParameters) >0 :
                model.set_params(taskParameters)

        df = self.dataset.df
        targetFeature = self.dataset.targetFeature
        y = df[targetFeature]
        X = df.drop(columns=[targetFeature])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        measures = []
        for measureProcedure in measureProcedures:
            measure = measureProcedure.evaluate(y_truth = y_test, y_pred = y_pred)
            measures.append(measure)

        return measures
    
    