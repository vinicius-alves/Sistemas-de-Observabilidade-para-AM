from ..DTO.DatabaseManager import *
from ..DTO.Task import Task
from ..DTO.Dataset import *
from sklearn.model_selection import train_test_split

class IrisClassificationTask(Task):
    

    def __init__(self, session, name= None, task_type= None, dataset= None, time_frame= None, idTask = None):
        dataset_repo = DatasetRepository(session)
        dataset = dataset_repo.get(1) # iris dataset
        dataset.data_to_df()
        super().__init__(name= name, task_type= 'Classification', dataset= dataset, time_frame= None, idTask = None)


    def execute(self, model, modelParameters, measureProcedures):

        if modelParameters is not None:
            model.setModelParameters(modelParameters)

        df = self.dataset.df
        targetFeature = self.dataset.targetFeature
        y = df[targetFeature]
        X = df.drop(columns=[targetFeature])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model.fit(X_train, y_train)
        prediction = model.predict(X_test)
        measures = []
        for measureProcedure in measureProcedures:
            measure = measureProcedure.evaluate(y_truth = y_test, y_pred = prediction)
            measures.append(measure)

        return measures