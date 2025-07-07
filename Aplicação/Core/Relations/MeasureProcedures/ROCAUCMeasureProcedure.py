from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import roc_auc_score
import numpy as np

class ROCAUCMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred_proba = kwargs.get("y_pred_proba", None) 
        value = roc_auc_score(y_truth, y_pred_proba)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='ROC AUC') , value= value, evaluationProcedure = self)