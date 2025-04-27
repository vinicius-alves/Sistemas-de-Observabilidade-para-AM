from .Parameter import Parameter
from .ParameterType import ParameterType

class Run():

    def execute(self, task, model, task_parameters = None, model_parameters = None):
        self.task = task
        self.model = model 

        self.parameters = []
        
        if type(model_parameters) == dict:
            self.model.set_params(model_parameters)
        predictions , measures= task.execute(model = model,  parameters = task_parameters)

        if predictions:
            self.predictions = predictions

        if measures:
            self.measures= measures

        self.parameters += self.model.get_params()

        if type(task_parameters) == dict:

            task_parameters_list = []
            for key, value in task_parameters.items():
                taskParameter = Parameter(name = key, value = value)
                taskParameter.parameterType = ParameterType(idParameterType = 2,name = 'Task')
                taskParameter.process_type()
                task_parameters_list.append(taskParameter)

            self.parameters += task_parameters_list

        

