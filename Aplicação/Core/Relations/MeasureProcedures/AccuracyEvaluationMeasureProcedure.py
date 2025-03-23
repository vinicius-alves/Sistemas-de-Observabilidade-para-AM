from ..EvaluationProcedure import EvaluationProcedure
from ..EvaluationMeasure import EvaluationMeasure
from sklearn.metrics import accuracy_score  

class AccuracyEvaluationMeasureProcedure(EvaluationProcedure):

    def __init__(self):
        self.name = 'AccuracyEvaluationMeasureProcedure'
        self.object = None 

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None)
        accuracy = accuracy_score(y_truth, y_pred)
        return EvaluationMeasure(name = 'accuracy', measureValue= accuracy)