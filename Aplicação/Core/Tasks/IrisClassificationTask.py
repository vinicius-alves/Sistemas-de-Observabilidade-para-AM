from ..DTO.DatabaseManager import *
from ..DTO.Task import Task
from ..DTO.Dataset import *
from sklearn.model_selection import train_test_split
from ..DTO.TaskType import *

class IrisClassificationTask(Task):
    

    def __init__(self, session,name= None, idTaskType= None, dataset= None, idTask = None):
        dataset_repo = DatasetRepository(session)
        dataset = dataset_repo.get(1) # iris dataset
        dataset.data_to_df()
        #self.task_type= 'Classification'
        self.idTask = idTask
        self.name = name
        self.idTaskType = idTaskType
        self.dataset = dataset


    def execute(self, model, taskParameters, measureProcedures):

        if taskParameters is not None:
            model.setModelParameters(taskParameters)

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