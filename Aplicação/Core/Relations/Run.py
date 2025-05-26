from .Parameter import Parameter
from .ParameterType import ParameterType

class Run():

    def __init__(self, project = None , task = None, model = None):
        self.project = project
        self.task = task
        self.model = model

    def execute(self,  task_parameters = None, model_parameters = None):
       
        self.parameters = []
        target_feature_name = self.project.targetFeature.get_full_name()
        self.task.set_target_feature_name(target_feature_name = target_feature_name)
        
        if type(model_parameters) == dict:
            self.model.set_params(model_parameters)
        predictions , measureValues= self.task.execute(model = self.model,  parameters = task_parameters)

        if predictions:
            self.predictions = predictions

        if measureValues:
            self.measureValues= measureValues

        self.parameters += self.model.get_params()

        if type(task_parameters) == dict:

            task_parameters_list = []
            for key, value in task_parameters.items():
                taskParameter = Parameter(name = key, value = value)
                taskParameter.parameterType = ParameterType(idParameterType = 2,name = 'Task')
                taskParameter.process_type()
                task_parameters_list.append(taskParameter)

            self.parameters += task_parameters_list

        if self.task.taskType.type == 'Training':
            self.featureImportances = self.model.feature_importances()

        

