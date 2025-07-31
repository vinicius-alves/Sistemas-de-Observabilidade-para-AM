from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from scipy.stats import kruskal
import numpy as np

class KruskalWallisMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        lst_arrays = kwargs.get("lst_arrays", None)
        stat, p = kruskal(*lst_arrays)
        value = np.round(p,5)
        if np.isnan(value):
            value =None
        return MeasureValue(measure = Measure(name='Kruskal Wallis'), value= value, evaluationProcedure = self)