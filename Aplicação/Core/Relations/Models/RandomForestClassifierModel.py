
from ..Model import Model 
from ..Parameter import Parameter
from ..ParameterType import ParameterType
from sklearn.ensemble import RandomForestClassifier
import sklearn 

class RandomForestClassifierModel(Model):

    def __init__(self):
        self.model = RandomForestClassifier()
        self.name = type(self).__name__
        self.version = sklearn.__version__
    
    def fit(self,X,y):
        self.model.fit(X,y)
        self.serialize()
    
    def predict(self,X):
        return self.model.predict(X)
        
    def predict_proba(self,X):
        return self.model.predict_proba(X)
    
    def set_params(self,params):
        self.model.set_params(**params)
        self.serialize()

    def get_params(self):
        params = self.model.get_params()
        lst_parameters = []
        for key, value in params.items():
            modelParameter = Parameter(name = key, value = value)
            modelParameter.parameterType = ParameterType(idParameterType = 1,name = 'Model')
            modelParameter.process_type()
            lst_parameters.append(modelParameter)
        return lst_parameters