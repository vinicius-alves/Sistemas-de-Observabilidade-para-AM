from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
import numpy as np

class SelectionRateMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_pred = kwargs.get("y_pred", None) 
        value = None
        if len(y_pred)>0:
            value = np.sum(y_pred == 1) / len(y_pred)
        return MeasureValue(measure = Measure(name='Selection Rate'), value= value, evaluationProcedure = self)