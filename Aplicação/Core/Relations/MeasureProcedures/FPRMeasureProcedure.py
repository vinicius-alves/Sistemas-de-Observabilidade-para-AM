from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import confusion_matrix

class FPRMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 

        tn, fp, fn, tp = confusion_matrix(y_truth, y_pred, labels=[0, 1]).ravel()
        fp_tn = fp + tn
        value = None 
        if fp_tn>0:
            value = fp / fp_tn
        return MeasureValue(measure = Measure(name='FPR'), value= value, evaluationProcedure = self)