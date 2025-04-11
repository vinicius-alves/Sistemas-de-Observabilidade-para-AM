from ..EvaluationProcedure import EvaluationProcedure
from ..Measure import Measure
from sklearn.metrics import mean_squared_error

class RMSEMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        rmse = mean_squared_error(y_truth, y_pred, squared=False)
        return Measure(name = 'rmse', value= rmse, evaluationProcedure = self)