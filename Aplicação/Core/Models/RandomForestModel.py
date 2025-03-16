from ..DTO.Model import Model  
from sklearn.ensemble import RandomForestClassifier
from ..DTO.Dataset import Dataset

class RandomForestModel(Model):

    def __init__(self):
        self.idModel = 1
        self.name = 'RandomForest'
        self.version = 1
        self.description = None
        self.clf = RandomForestClassifier(n_estimators=100, random_state=42)

    def setModelParameters(self,modelParameters):
        if modelParameters is not None:
            self.clf = RandomForestClassifier(*modelParameters)
    
    def fit(self,X,y): 
        self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict (X) 

    def predict_proba(self, X):
        return self.clf.predict_proba(X)