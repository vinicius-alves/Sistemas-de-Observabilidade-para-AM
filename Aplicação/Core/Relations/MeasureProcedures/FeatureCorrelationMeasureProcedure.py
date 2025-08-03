from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from ..Feature import Feature
from ..SubjectFeature import SubjectFeature
import numpy as np

class FeatureCorrelationMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs): 
        df_current = kwargs.get("df_current", None).drop(columns=['timestamp','idEntity'], errors = 'ignore')
        name_space_map  = kwargs.get("name_space_map", None) 

        
        corr = df_current.corr(method='spearman', numeric_only=True)

        # Obter pares abaixo da diagonal principal
        cols = corr.columns
        measureValues = []
        for i in range(1, len(cols)):
            for j in range(i):
                feature1 = cols[i]
                feature2 = cols[j]
                value = corr.iloc[i, j]

                if np.isnan(value):
                    continue
                
                name_space_obj = name_space_map[feature1]
                name_space_id = name_space_obj.idFeatureNameSpace
                feature_reference1 = Feature(name = feature1, nameSpace=name_space_obj, idFeatureNameSpace = name_space_id)

                name_space_obj = name_space_map[feature2]
                name_space_id = name_space_obj.idFeatureNameSpace
                feature_reference2 = Feature(name = feature2, nameSpace=name_space_obj, idFeatureNameSpace = name_space_id)

                measure = Measure(name = 'Correlation' )
                measure.subjectFeatures = [SubjectFeature(feature=feature_reference1),SubjectFeature(feature=feature_reference2)]

                measureValue = MeasureValue(measure=measure, value = value, evaluationProcedure= self) 
                measureValues.append(measureValue)


        return measureValues 