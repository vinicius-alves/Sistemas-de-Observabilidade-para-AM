import pickle, io

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
    
    def serialize(self):
        if self.model is not None:
            buffer = io.BytesIO()
            pickle.dump(self.model, buffer)
            self.object = buffer.getvalue()

    def deserialize(self):
        if self.object is not None:
            self.model =  pickle.loads(self.object)

    # automatic serialize
    @property
    def model(self):
        return self.__dict__["model"] 

    @model.setter
    def model(self, novo_valor):
       if novo_valor != self.__dict__.get("model", None):
        self.__dict__["model"] = novo_valor  
        self.serialize()

    # automatic deserialize
    @property
    def object(self):
        return self.__dict__["object"]  

    @object.setter
    def object(self, novo_valor):
       if novo_valor != self.__dict__.get("object", None):
           self.__dict__["object"] = novo_valor 
           self.deserialize()