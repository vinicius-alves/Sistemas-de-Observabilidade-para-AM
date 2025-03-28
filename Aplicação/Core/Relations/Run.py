class Run():

    def execute(self, task, model, taskParameters):
        self.task = task
        self.model = model
        self.taskParameters = taskParameters
        self.measures = task.execute(model = model,  taskParameters = taskParameters)

