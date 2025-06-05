from ..EvaluationProcedure import EvaluationProcedure
from ..MeasureValue import MeasureValue
from ..Measure import Measure
from ..Feature import Feature
from ..SubjectFeature import SubjectFeature
from evidently.legacy.report import Report
from evidently.legacy.metrics import ColumnDriftMetric
import pandas as pd

class JSMeasureProcedure(EvaluationProcedure):

    def evaluate(self, **kwargs):
        df_reference = kwargs.get("df_reference", None)
        df_current = kwargs.get("df_current", None) 
        name_space_map  = kwargs.get("name_space_map", None) 

        columns = df_reference.columns.tolist()
        report = Report(
            metrics=[
                ColumnDriftMetric(column_name=col, stattest='jensenshannon') for col in columns
            ]
        )
        report.run(reference_data=df_reference, current_data=df_current)

        report_dict = report.as_dict()
        results = []
        for metric_result in report_dict['metrics']:
            column_result = metric_result['result']
            results.append({
                'column_name': column_result['column_name'],
                'drift_detected': column_result['drift_detected'],
                'stattest_name': column_result['stattest_name'],
                'drift_score': column_result['drift_score'],
            })
        df_results = pd.DataFrame(results)    
        df_results['drift_detected'] = df_results['drift_detected'].astype('int')
        
        def create_feature(feature_name):
            name_space_obj = name_space_map[feature_name]
            name_space_id = name_space_obj.idFeatureNameSpace
            return  Feature(name = feature_name, nameSpace=name_space_obj, idFeatureNameSpace = name_space_id)

        df_results['feature_reference'] = df_results['column_name'].map(create_feature)

        def calc_drift_measure(record):
            feature_reference = record['feature_reference']
            measure = Measure(name = 'drift' +' ' + feature_reference.nameSpace.name + ' ' +feature_reference.name)
            measure.subjectFeatures = [SubjectFeature(feature=feature_reference)]
            measureValue = MeasureValue(measure=measure, value = record['drift_detected'], evaluationProcedure= self)
            return measureValue

        def calc_specif_measure(record):
            feature_reference = record['feature_reference']
            measure = Measure(name = record['stattest_name'] +' '+feature_reference.nameSpace.name + ' ' +feature_reference.name)
            measure.subjectFeatures = [SubjectFeature(feature=feature_reference)]
            measureValue = MeasureValue(measure=measure, value = record['drift_score'], evaluationProcedure= self)
            return measureValue

        df_results['drift_measure'] = df_results.apply(calc_drift_measure, axis = 1)
        df_results['specif_measure'] = df_results.apply(calc_specif_measure, axis = 1)

        measureValues = df_results['drift_measure'].to_list() + df_results['specif_measure'].to_list()

        return measureValues 