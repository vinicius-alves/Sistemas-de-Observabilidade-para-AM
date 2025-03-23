class Run():

    def execute(self, task, measureProcedures, model, taskParameters):
        self.task = task
        self.model = model
        self.taskParameters = taskParameters
        self.measures = task.execute(model,  measureProcedures = measureProcedures, taskParameters = taskParameters)

