from .Parameter import Parameter
from .ParameterType import ParameterType

class Run():

    def execute(self, task, model, taskParameters = None, modelParameters = None):
        self.task = task
        self.model = model 

        self.parameters = []
        
        if type(modelParameters) == dict:
            self.model.set_params(modelParameters)
        predictions , measures= task.execute(model = model,  parameters = taskParameters)

        if predictions:
            self.predictions = predictions

        if measures:
            self.measures= measures

        self.parameters += self.model.get_params()

        if type(taskParameters) == dict:

            taskParameters_list = []
            for key, value in taskParameters.items():
                taskParameter = Parameter(name = key, value = value)
                taskParameter.parameterType = ParameterType(idParameterType = 2,name = 'Task')
                taskParameter.process_type()
                taskParameters_list.append(taskParameter)

            self.parameters += taskParameters_list

        

