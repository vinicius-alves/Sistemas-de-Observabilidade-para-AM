from ..EvaluationProcedure import EvaluationProcedure
from ..Measure import Measure
from sklearn.metrics import mean_absolute_error

class MAEMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        y_truth = kwargs.get("y_truth", None)
        y_pred = kwargs.get("y_pred", None) 
        rmse = mean_absolute_error(y_truth, y_pred)
        return Measure(name = 'MAE', value= rmse, evaluationProcedure = self)