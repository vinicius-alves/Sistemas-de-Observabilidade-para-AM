from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from scipy.stats import ks_2samp
import numpy as np

class KSMeasureProcedure(EvaluationProcedure):

    def ks_statistic(self, y_true, y_score):
        pos_scores = y_score[y_true == 1]
        neg_scores = y_score[y_true == 0]
        stat, p_value = ks_2samp(pos_scores, neg_scores)
        return stat

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred_proba = kwargs.get("y_pred_proba", None) 

        value =  self.ks_statistic(y_truth,y_pred_proba)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='KS') , value= value, evaluationProcedure = self)