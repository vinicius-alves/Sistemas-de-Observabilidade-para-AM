from .ModelParameter import ModelParameter
from .TaskParameter import TaskParameter

class Run():

    def execute(self, task, model, taskParameters = None, modelParameters = None):
        self.task = task
        self.model = model
        
        model.set_params(modelParameters)
        self.measures = task.execute(model = model,  taskParameters = taskParameters)

        if type(modelParameters) == dict:

            modelParameters_list = []
            for key, value in modelParameters.items():
                modelParameter = ModelParameter(name = key, value = value)
                modelParameter.process_type()
                modelParameters_list.append(modelParameter)

            self.modelParameters = modelParameters_list

        if type(taskParameters) == dict:

            taskParameters_list = []
            for key, value in taskParameters.items():
                taskParameter = TaskParameter(name = key, value = value)
                taskParameter.process_type()
                taskParameters_list.append(taskParameter)

            self.taskParameters = taskParameters_list

        

