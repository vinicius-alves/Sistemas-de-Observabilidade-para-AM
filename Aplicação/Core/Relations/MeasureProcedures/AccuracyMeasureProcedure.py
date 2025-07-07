from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import accuracy_score  
import numpy as np

class AccuracyMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None)
        value = accuracy_score(y_truth, y_pred)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='Accuracy'), value= value, evaluationProcedure = self)