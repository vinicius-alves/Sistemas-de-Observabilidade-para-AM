
class Model():


    def __init__(self):
        raise NotImplementedError('Classe abstrata')
    
    def fit(self,X,y):
        raise NotImplementedError('Classe abstrata')
    
    def predict(self,X):
        raise NotImplementedError('Classe abstrata')
    
    def predict_proba(self,X):
        raise NotImplementedError('Classe abstrata')
    
    def set_params(**kwargs):
        raise NotImplementedError('Classe abstrata')
    
    def get_params(self):
        raise NotImplementedError('Classe abstrata')