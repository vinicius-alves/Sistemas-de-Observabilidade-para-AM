from .Parameter import Parameter

class Run():

    def execute(self, task, model, parameters = None):
        self.task = task
        self.model = model

        modelParameters = parameters
        taskParameters = parameters
        
        self.model.set_params(modelParameters)
        self.measures = task.execute(model = model,  parameters = taskParameters)
        self.modelParameters = self.model.get_params()

        if type(taskParameters) == dict:

            taskParameters_list = []
            for key, value in taskParameters.items():
                taskParameter = Parameter(name = key, value = value)
                taskParameter.process_type()
                taskParameters_list.append(taskParameter)

            self.taskParameters = taskParameters_list

        

