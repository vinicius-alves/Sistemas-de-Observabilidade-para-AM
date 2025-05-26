from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import log_loss

class LogLossMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        rmse = log_loss(y_truth, y_pred)
        return MeasureValue(name = Measure(name='Log Loss') , value= rmse, evaluationProcedure = self)