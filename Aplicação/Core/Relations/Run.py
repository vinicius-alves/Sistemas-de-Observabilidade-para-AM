class Run():

    def execute(self, task, model, taskParameters = None, modelParameters = None):
        self.task = task
        self.model = model
        self.taskParameters = taskParameters
        self.modelParameters = modelParameters

        if modelParameters is not None:
            if len(modelParameters) >0 :
                model.set_params(modelParameters)

        self.measures = task.execute(model = model,  taskParameters = taskParameters)

