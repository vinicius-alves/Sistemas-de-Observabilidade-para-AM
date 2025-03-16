from ..DTO.Model import Model  
from sklearn.ensemble import RandomForestClassifier

class RandomForestModel(Model):


    def __init__(self):
        self.idModel = None
        self.name = 'RandomForestClassifier'
        self.version = 1 
        self.object = None
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