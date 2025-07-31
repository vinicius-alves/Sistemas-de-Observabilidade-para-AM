from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import brier_score_loss
import numpy as np

class BrierScoreMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred_proba = kwargs.get("y_pred_proba", None) 
        value = brier_score_loss(y_truth, y_pred_proba)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='Brier Score') , value= value, evaluationProcedure = self)