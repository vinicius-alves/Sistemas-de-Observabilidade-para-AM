
from ..Model import Model 
from ..ModelParameter import ModelParameter
from sklearn.ensemble import RandomForestClassifier

class RandomForestClassifierModel(Model):


    def __init__(self):
        self.clf = RandomForestClassifier()
        self.name = 'RandomForestClassifierModel'
    
    def fit(self,X,y):
        self.clf.fit(X,y)
    
    def predict(self,X):
        return self.clf.predict(X)
        
    def predict_proba(self,X):
        return self.clf.predict_proba(X)
    
    def set_params(self,params):
        self.clf.set_params(**params)

    def get_params(self):
        params = self.clf.get_params()
        lst_modelParameters = []
        for key, value in params.items():
            modelParameter = ModelParameter(name = key, value = value)
            modelParameter.process_type()
            lst_modelParameters.append(modelParameter)
        return lst_modelParameters