from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from ..Feature import Feature
from ..SubjectFeature import SubjectFeature
import pandas as pd

class FeatureMissingMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs): 
        df_current = kwargs.get("df_current", None).drop(columns=['timestamp','idEntity'], errors = 'ignore')
        name_space_map  = kwargs.get("name_space_map", None) 

        serie_missing = df_current.isnull().mean() * 100
        df_missing = pd.DataFrame(serie_missing.values, serie_missing.index).T
        dict_missing = df_missing.to_dict(orient = 'records')[0]
        measureValues = []
        for feature_name, missing_pc in dict_missing.items():
            name_space_obj = name_space_map[feature_name]
            name_space_id = name_space_obj.idFeatureNameSpace
            feature_reference = Feature(name = feature_name, nameSpace=name_space_obj, idFeatureNameSpace = name_space_id)
            measure = Measure(name = 'Missing PC' +' ' + feature_reference.nameSpace.name + ' ' +feature_reference.name)
            measure.subjectFeatures = [SubjectFeature(feature=feature_reference)]
            measureValue = MeasureValue(measure=measure, value = missing_pc, evaluationProcedure= self) 
            measureValues.append(measureValue)

        return measureValues 