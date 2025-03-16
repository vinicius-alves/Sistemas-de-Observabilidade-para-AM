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
        self.clf = RandomForestClassifier(*modelParameters)
    
    def fit(self,X,y):
        #df = data.df
        #X = df.drop(columns=[data.targetFeature])
        #y = df[data.targetFeature]    
        self.clf.fit(X, y)

    def predict(self, X):
        #df = data.df
        #X = df.drop(columns=[data.targetFeature], errors ='ignore')
        return self.clf.predict (X) 

    def predict_proba(self, X):
        #df = data.df
        #X = df.drop(columns=[data.targetFeature], errors ='ignore')
        return self.clf.predict_proba(X)