from .Parameter import Parameter
from .ParameterType import ParameterType

class Run():

    def __init__(self, project = None , dataset = None, task = None, model = None):
        self.project = project
        self.task = task
        self.model = model
        self.dataset = dataset

    def execute(self,  task_parameters = None, model_parameters = None):

        self.task.set_dataset(self.dataset)
       
        self.parameters = []
        target_feature_name = self.project.targetFeature.get_full_name()
        self.task.set_target_feature_name(target_feature_name = target_feature_name)
        
        if type(model_parameters) == dict and self.model:
            self.model.set_params(model_parameters)

        self.task.set_model(self.model)
        predictions , measureValues= self.task.execute(parameters = task_parameters)

        if predictions:
            self.predictions = predictions

        if measureValues:
            self.measureValues= measureValues

        if self.model:
            self.parameters += self.model.get_params()

        if type(task_parameters) == dict:

            task_parameters_list = []
            for key, value in task_parameters.items():
                taskParameter = Parameter(name = key, value = value)
                taskParameter.parameterType = ParameterType(idParameterType = 2,name = 'Task')
                taskParameter.process_type()
                task_parameters_list.append(taskParameter)

            self.parameters += task_parameters_list

        if self.task.taskType.type == 'Training' and self.model:
            self.featureImportances = self.model.feature_importances()

        

