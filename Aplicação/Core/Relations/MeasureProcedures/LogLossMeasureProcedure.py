from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import log_loss
import numpy as np

class LogLossMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        value = log_loss(y_truth, y_pred, labels=[0, 1])
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='Log Loss') , value= value, evaluationProcedure = self)