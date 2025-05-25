from ..EvaluationProcedure import EvaluationProcedure
from ..Measure import Measure
from sklearn.metrics import root_mean_squared_error

class RMSEMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        rmse = root_mean_squared_error(y_truth, y_pred)
        return Measure(name = 'RMSE', value= rmse, evaluationProcedure = self)