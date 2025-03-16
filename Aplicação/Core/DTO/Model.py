from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, Float, LargeBinary
from sqlalchemy.orm import relationship
from .Dataset import Dataset

class Model(Base):
    __tablename__ = 'model'

    idModel = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    version = Column(Float, nullable=True)
    object = Column(LargeBinary, nullable=True)

    runs = relationship('Run', back_populates='model')

    def __init__(self, name, version, object, idModel = None):
        self.idModel = idModel
        self.name = name
        self.version = version
        self.object = object

    def fit(self, data : Dataset):
        raise NotImplementedError('Base class method')

    def predict(self, data: Dataset):
        raise NotImplementedError('Base class method')

    def predict_proba(self, data: Dataset):
        raise NotImplementedError('Base class method')

    def setModelParameters(self,modelParameters):
        raise NotImplementedError('Base class method')


# 🔹 Repositório específico para Dataset (herda de GenericRepository)
class ModelRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Model)