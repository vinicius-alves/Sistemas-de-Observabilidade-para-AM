
from ..Model import Model 
from ..Parameter import Parameter
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
        lst_parameters = []
        for key, value in params.items():
            modelParameter = Parameter(name = key, value = value)
            modelParameter.process_type()
            lst_parameters.append(modelParameter)
        return lst_parameters