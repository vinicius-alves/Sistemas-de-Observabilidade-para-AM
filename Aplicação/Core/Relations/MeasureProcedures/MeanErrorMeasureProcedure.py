from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
import numpy as np

class MeanErrorMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        value = np.mean(y_pred - y_truth)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='Mean Error'), value= value, evaluationProcedure = self)