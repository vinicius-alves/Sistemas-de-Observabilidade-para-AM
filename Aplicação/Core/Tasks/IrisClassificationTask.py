from ..DTO.DatabaseManager import *
from ..DTO.TaskDTO import TaskDTO
from ..DTO.TaskTypeDTO import *
from ..DTO.DatasetDTO import *
from sklearn.model_selection import train_test_split
from ..DTO.TaskTypeDTO import *

class IrisClassificationTaskDTO(TaskDTO):

    pass
    '''
    

    def __init__(self, session, idTaskType= None, DatasetDTO= None, idTask = None):
        DatasetDTO_repo = DatasetRepository(session)
        DatasetDTO = DatasetDTO_repo.get(1) # iris DatasetDTO
        DatasetDTO.data_to_df()

        TaskDTO_type_repo = TaskTypeRepository(session= session)
        self.TaskTypeDTO = TaskDTO_type_repo.get(1)
        self.name = 'IrisClassificationTaskDTO'
        self.idTaskType = idTaskType
        self.DatasetDTO = DatasetDTO


    def execute(self, model, taskParameters, measureProcedures):

        if taskParameters is not None:
            model.setModelDTOParameters(taskParameters)

        df = self.DatasetDTO.df
        targetFeature = self.DatasetDTO.targetFeature
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
    '''