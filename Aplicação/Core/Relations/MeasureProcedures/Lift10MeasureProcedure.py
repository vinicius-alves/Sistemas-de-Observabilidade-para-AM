from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
import numpy as np

class Lift10MeasureProcedure(EvaluationProcedure):

    def lift_at_k(self, y_true, y_score, k=0.1):
        n = len(y_true)
        cutoff = int(n * k)
        
        idx_sorted = np.argsort(y_score)[::-1]
        top_k_idx = idx_sorted[:cutoff]
        
        positives_top_k = y_true[top_k_idx].sum()
        base_rate = y_true.mean()
        top_k_rate = positives_top_k / cutoff

        lift = top_k_rate / base_rate if base_rate > 0 else np.nan
        return lift

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred_proba = kwargs.get("y_pred_proba", None) 

        y_truth = np.array(y_truth)
        y_pred_proba =np.array(y_pred_proba)
        
        value =  self.lift_at_k(y_truth, y_pred_proba, k=0.10)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='Lift 10') , value= value, evaluationProcedure = self)