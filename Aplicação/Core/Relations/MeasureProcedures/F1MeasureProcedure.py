from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import f1_score
import numpy as np

class F1MeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        value = f1_score(y_truth, y_pred, zero_division = np.nan)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='F1') , value= value, evaluationProcedure = self)