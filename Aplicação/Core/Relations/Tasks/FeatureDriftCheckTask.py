from ..Task import *
from ..TaskType import * 
from ..EvaluationProcedure import *
from ..Measure import *
from ..MeasureValue import *
from ..SubjectFeature import *
from ..Feature import *
from evidently.legacy.report import Report
from evidently.legacy.metric_preset  import DataDriftPreset 
import pandas as pd

class FeatureDriftCheckTask(Task):

   
    def __init__(self,   dataset= None):
        self.taskType = TaskType(type = 'Others')
        self.name = type(self).__name__
        self.dataset = dataset

    def execute(self, model=None, parameters= {}):

        df = self.dataset.df.drop(columns = ['idEntity'], errors='ignore') 

        if not(isinstance(parameters,dict)):
            return
    
        df_reference = df[df['timestamp']<pd.Timestamp(parameters['end_reference_date'])].drop(columns = ['timestamp'], errors='ignore')
        df_current = df[(df['timestamp']>=pd.Timestamp(parameters['start_current_date'])) & (df['timestamp']<=pd.Timestamp(parameters['end_current_date']))].drop(columns = ['timestamp'], errors='ignore')

        report = Report(metrics=[DataDriftPreset()])
        report.run(reference_data=df_reference, current_data=df_current)

        results = report.as_dict()

        drift_results = results['metrics'][1]['result']['drift_by_columns']
        df_results = pd.DataFrame(drift_results.values())
        df_results.drop(columns=['current','reference','stattest_threshold','column_type'], inplace = True)
        df_results['drift_detected'] = df_results['drift_detected'].astype('int')
        df_results['feature_reference'] = df_results['column_name'].map(lambda x: Feature(name = x))


        def calc_drift_measure(record):
            feature_reference = record['feature_reference']
            measure = Measure(name = 'drift')
            measure.subjectFeatures = [SubjectFeature(feature=feature_reference, measure = measure)]
            measureValue = MeasureValue(measure=measure, value = record['drift_detected'], evaluationProcedure= EvaluationProcedure(name = record['stattest_name'] + ' Threshold'))
            return measureValue

        def calc_specif_measure(record):
            feature_reference = record['feature_reference']
            measure = Measure(name = record['stattest_name'])
            measure.subjectFeatures = [SubjectFeature(feature=feature_reference, measure = measure)]
            measureValue = MeasureValue(measure=measure, value = record['drift_score'], evaluationProcedure= EvaluationProcedure(name = record['stattest_name']))
            return measureValue

        df_results['drift_measure'] = df_results.apply(calc_drift_measure, axis = 1)
        df_results['specif_measure'] = df_results.apply(calc_specif_measure, axis = 1)

        measureValues = df_results['drift_measure'].to_list() + df_results['specif_measure'].to_list()

        return None, measureValues
    
    