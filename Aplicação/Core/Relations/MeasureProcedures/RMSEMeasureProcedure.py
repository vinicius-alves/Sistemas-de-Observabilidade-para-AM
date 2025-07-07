from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from sklearn.metrics import root_mean_squared_error
import numpy as np

class RMSEMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        value = root_mean_squared_error(y_truth, y_pred)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='RMSE'), value= value, evaluationProcedure = self)