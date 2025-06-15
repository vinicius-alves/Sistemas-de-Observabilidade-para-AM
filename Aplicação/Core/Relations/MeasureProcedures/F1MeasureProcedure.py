from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import f1_score

class F1MeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        value = f1_score(y_truth, y_pred)
        return MeasureValue(measure = Measure(name='F1') , value= value, evaluationProcedure = self)