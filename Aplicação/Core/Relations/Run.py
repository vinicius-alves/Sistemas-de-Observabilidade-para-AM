from .TaskParameter import TaskParameter

class Run():

    def execute(self, task, model, taskParameters = None, modelParameters = None):
        self.task = task
        self.model = model
        
        self.model.set_params(modelParameters)
        self.measures = task.execute(model = model,  taskParameters = taskParameters)
        self.modelParameters = self.model.get_params()

        if type(taskParameters) == dict:

            taskParameters_list = []
            for key, value in taskParameters.items():
                taskParameter = TaskParameter(name = key, value = value)
                taskParameter.process_type()
                taskParameters_list.append(taskParameter)

            self.taskParameters = taskParameters_list

        

