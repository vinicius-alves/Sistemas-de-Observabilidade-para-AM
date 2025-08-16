from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from ..SubjectEntity import SubjectEntity
from sklearn.ensemble import IsolationForest
import pandas as pd

class IsolationForestEvaluationProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        df_reference = kwargs.get("df_reference", None) 
        df_current = kwargs.get("df_current", None) 

        cols_to_drop = df_reference.select_dtypes(exclude=['number']).columns.tolist()
        cols_to_drop += ['idEntity', 'timestamp']

        df_reference.drop(columns = cols_to_drop, errors='ignore', inplace =True)
        
        clf = IsolationForest(random_state=0, contamination=0.05,n_estimators=200,max_samples=0.05)
        clf.fit(df_reference)
        df_current['value'] = clf.predict(df_current.drop(columns = cols_to_drop, errors='ignore'))
        df_current['subjectEntity'] = df_current.apply(lambda x: SubjectEntity(**x), axis =1)

        def calc_measure(record):
            subject_entity = record['subjectEntity']
            measure = Measure(name = 'Outlier')
            measure.subjectEntities = [subject_entity]
            measureValue = MeasureValue(measure=measure, value = record['value'], evaluationProcedure= self)
            return measureValue

        df_current['measureValue'] = df_current.apply(calc_measure, axis = 1)

        measureValues = df_current['measureValue'].to_list()

        return measureValues 