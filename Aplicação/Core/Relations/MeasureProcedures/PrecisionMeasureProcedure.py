from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import precision_score
import numpy as np

class PrecisionMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        value = precision_score(y_truth, y_pred, zero_division = np.nan)
        return MeasureValue(measure = Measure(name='Precision') , value= value, evaluationProcedure = self)