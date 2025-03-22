from ..DTO.EvaluationProcedureDTO import EvaluationProcedureDTO
from ..DTO.EvaluationMeasureDTO import EvaluationMeasureDTO
from sklearn.metrics import accuracy_score  

class AccuracyMeasureProcedure(EvaluationProcedureDTO):

    def __init__(self):
        self.name = 'AccuracyMeasureProcedure'
        self.object = None 

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None)
        accuracy = accuracy_score(y_truth, y_pred)
        return EvaluationMeasureDTO(name = 'accuracy', measureValue= accuracy)