class EvaluationMeasure:
    def __init__(self, measure_id, name, description):
        self.measure_id = measure_id
        self.name = name
        self.description = description
    
    def compute(self, dataset, flow):
        pass