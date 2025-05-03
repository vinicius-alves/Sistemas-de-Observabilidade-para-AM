
from ..Model import Model 
from ..Parameter import Parameter
from ..ParameterType import ParameterType
from ..FeatureImportance import FeatureImportance
from ..Feature import Feature
from ..FeatureNameSpace import FeatureNameSpace
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor 
import sklearn 

class OHEDecisionTreeRegressor(Model):

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
            ("regressor", DecisionTreeRegressor(random_state=42))
        ])

    def feature_importances(self): 
        ohe = self.model.named_steps["preprocessor"].named_transformers_["cat"] 
        ohe_feature_names = ohe.get_feature_names_out(self.categorical_cols)
 
        feature_names = list(ohe_feature_names) + self.numeric_cols
 
        importances = self.model.named_steps["regressor"].feature_importances_
        feature_importances = []
        featureNameSpace = FeatureNameSpace()
        for feature_name, importance in zip(feature_names,importances):
            feature = Feature(name = feature_name, nameSpace = featureNameSpace)
            record = FeatureImportance(feature=feature, importance= importance)
            feature_importances.append(record)
        return feature_importances
         
    
    def fit(self,X,y):
        self.create_pipeline(X)
        self.model.fit(X,y)
        self.serialize()
    
    def predict(self,X):
        return self.model.predict(X)
        
    def predict_proba(self,X):
        return self.model.predict_proba(X)
    
    def set_params(self,params):
        self.model.named_steps['regressor'].set_params(**params)
        self.serialize()

    def get_params(self):
        params = self.model.named_steps['regressor'].get_params()
        lst_parameters = []
        for key, value in params.items():           
            modelParameter = Parameter(name = key, value = value)
            modelParameter.parameterType = ParameterType(idParameterType = 1,name = 'Model')
            modelParameter.process_type()
            lst_parameters.append(modelParameter)
        return lst_parameters