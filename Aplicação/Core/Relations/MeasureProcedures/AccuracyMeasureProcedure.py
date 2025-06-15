from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import accuracy_score  

class AccuracyMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None)
        value = accuracy_score(y_truth, y_pred)
        return MeasureValue(measure = Measure(name='Accuracy'), value= value, evaluationProcedure = self)