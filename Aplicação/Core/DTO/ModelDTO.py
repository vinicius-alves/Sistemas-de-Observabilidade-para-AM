from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, Float, LargeBinary
from sqlalchemy.orm import relationship
import pickle, io

class ModelDTO(Base):
    __tablename__ = 'Model'

    idModel = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    version = Column(Float, nullable=True)
    object = Column(LargeBinary, nullable=True)

    runs = relationship('RunDTO', back_populates='model')

    def __init__(self, name = None, version = None, model = None, object = None, idModel = None):
        self.idModel = idModel
        self.name = name
        self.version = version
        self.object = object
        self.model = model

    def get_secondary_key(self):
        return 'name'

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
    


# 🔹 Repositório específico para DatasetDTO (herda de GenericRepository)
class ModelRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, ModelDTO)