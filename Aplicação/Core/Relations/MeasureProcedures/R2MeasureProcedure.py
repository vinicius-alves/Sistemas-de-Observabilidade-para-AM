from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import r2_score
import numpy as np

class R2MeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        value = r2_score(y_truth, y_pred)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='R2'), value= value, evaluationProcedure = self)