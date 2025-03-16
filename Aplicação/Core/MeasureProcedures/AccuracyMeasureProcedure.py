from ..DTO.EvaluationProcedure import EvaluationProcedure
from ..DTO.EvaluationMeasure import EvaluationMeasure
from sklearn.metrics import accuracy_score  

class AccuracyMeasureProcedure(EvaluationProcedure):

    def __init__(self):
        self.name = 'AccuracyMeasureProcedure'
        self.scriptEvaluation = None 

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None)
        accuracy = accuracy_score(y_truth, y_pred)
        return EvaluationMeasure(description = 'accuracy', measureValue= accuracy)