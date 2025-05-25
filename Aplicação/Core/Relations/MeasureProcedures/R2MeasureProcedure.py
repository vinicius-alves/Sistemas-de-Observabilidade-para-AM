from ..EvaluationProcedure import EvaluationProcedure
from ..Measure import Measure
from sklearn.metrics import r2_score

class R2MeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        rmse = r2_score(y_truth, y_pred)
        return Measure(name = 'R2', value= rmse, evaluationProcedure = self)