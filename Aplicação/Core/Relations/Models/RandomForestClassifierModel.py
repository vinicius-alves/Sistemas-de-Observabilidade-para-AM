
from ..Model import Model 
from sklearn.ensemble import RandomForestClassifier

class RandomForestClassifierModel(Model):


    def __init__(self):
        self.clf = RandomForestClassifier()
    
    def fit(self,X,y):
        self.clf.fit(X,y)
    
    def predict(self,X):
        return self.clf.predict(X)
        
    def predict_proba(self,X):
        return self.clf.predict_proba(X)
    
    def set_params(self,params):
        self.clf.set_params(**params)