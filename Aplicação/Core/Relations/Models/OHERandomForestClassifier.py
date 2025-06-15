
from ..Model import Model 
from ..Parameter import Parameter
from ..ParameterType import ParameterType
from ..FeatureImportance import FeatureImportance
from ..Feature import Feature
from ..Prediction import *
from ..PredictionFeatureContribution import *
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier 
import sklearn
import shap
import pandas as pd

class OHERandomForestClassifier(Model):

    def __init__(self): 
        self.name = type(self).__name__
        self.version = sklearn.__version__
        self.nameSpace = None
    
    def create_pipeline(self,X):
        self.categorical_cols = X.select_dtypes(include=["category", "object"]).columns.tolist()
        self.numeric_cols = X.select_dtypes(include=["number"]).columns.tolist()
        preprocessor = ColumnTransformer(
            transformers=[
                ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), self.categorical_cols)
            ],
            remainder="passthrough"
        )

        # Pipeline com DecisionTreeRegressor
        self.model = Pipeline(steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(random_state=42))
        ])

    def feature_names(self):

        ohe = self.model.named_steps["preprocessor"].named_transformers_["cat"] 
        ohe_feature_names = ohe.get_feature_names_out(self.categorical_cols)
        feature_names = list(ohe_feature_names) + self.numeric_cols
        return feature_names


    def feature_importances(self): 
   
        feature_names = self.feature_names()
        importances = self.model.named_steps["classifier"].feature_importances_
        feature_importances = []
        for feature_name, importance in zip(feature_names,importances):
            feature = Feature(name = feature_name)
            record = FeatureImportance(feature=feature, importance= importance)
            feature_importances.append(record)
        return feature_importances
    
    def explain_predictions(self,predictions,X):
        preprocessor = self.model.named_steps['preprocessor']
        classifier = self.model.named_steps['classifier']

        feature_names = self.feature_names()

        X_transformed = preprocessor.transform(X)
        explainer = shap.Explainer(classifier, X_transformed, feature_names=feature_names)
        shap_values = explainer(X_transformed,  check_additivity=False)

        class_idx = list(classifier.classes_).index(1)
        shap_class1 = shap_values.values[:, :, class_idx]

        shap_df = pd.DataFrame(shap_class1, columns=feature_names)
        shap_df['prediction_i'] = range(len(shap_df))

        shap_df['bias'] = shap_values.base_values[:, class_idx]

        extended_feature_names = feature_names + ['bias']

        shap_df_long = shap_df.melt(id_vars='prediction_i', var_name='feature', value_name='contribution')
        shap_df_long.sort_values(by = ['prediction_i','feature'], ignore_index=True, inplace=True)

        shap_df_long['obj'] = shap_df_long.apply(lambda x: PredictionFeatureContribution(feature= Feature(name  = x['feature']), contribution= x['contribution']) ,axis = 1)
        contributions = shap_df_long.pivot(index='prediction_i', columns='feature', values='obj')[extended_feature_names].values
 
        for i in range(len(predictions)):
            prediction = predictions[i]
            prediction.predictionFeatureContributions = list(contributions[i])

        return predictions
         
    
    def fit(self,X,y):
        X = X.drop(columns = ['timestamp','idEntity'], errors = 'ignore')
        self.create_pipeline(X)
        self.model.fit(X,y)
        self.serialize()
    
    def predict(self,X, generate_explanations = False):
        X_pred = X.drop(columns = ['timestamp','idEntity'], errors = 'ignore')
        y_pred= self.model.predict(X_pred)
        X['value'] = y_pred
        X['type'] = 'float'

        predictions = X.apply(lambda x : Prediction(**x), axis = 1).to_list()
        if generate_explanations:
            predictions =self.explain_predictions(predictions, X)


        return predictions
    

    def predict_proba(self, X):

        classifier = self.model.named_steps['classifier']
        class_idx = list(classifier.classes_).index(1)
        return self.model.predict_proba(X)[:, class_idx]
        
    
    def set_params(self,params):
        self.model.named_steps['classifier'].set_params(**params)
        self.serialize()

    def get_params(self):
        params = self.model.named_steps['classifier'].get_params()
        lst_parameters = []
        for key, value in params.items():           
            modelParameter = Parameter(name = key, value = value)
            modelParameter.parameterType = ParameterType(idParameterType = 1,name = 'Model')
            modelParameter.process_type()
            lst_parameters.append(modelParameter)
        return lst_parameters