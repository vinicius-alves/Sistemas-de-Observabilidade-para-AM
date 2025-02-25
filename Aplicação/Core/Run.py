class Run:
    def __init__(self, run_id, task, model, dataset, parameters):
        self.run_id = run_id
        self.task = task
        self.model = model
        self.dataset = dataset
        self.parameters = parameters
        self.results = {}

    def execute(self):
        pass
        #self.model.train(self.dataset)
        #predictions = self.model.predict(self.dataset)
        #return predictions
    
    def evaluate(self, evaluation_measures):
        for measure in evaluation_measures:
            self.results[measure.name] = measure.compute(self.dataset, self.model)
        return self.results