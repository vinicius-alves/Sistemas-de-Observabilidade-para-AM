from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from .Dataset import Dataset

class Model(Base):
    __tablename__ = 'model'

    idModel = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    version = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=True)

    runs = relationship('Run', back_populates='model')

    def __init__(self, name, version, description, idModel = None):
        self.idModel = idModel
        self.name = name
        self.version = version
        self.description = description

    def fit(self, data : Dataset):
        pass

    def predict(self, data: Dataset):
        pass

    def predict_proba(self, data: Dataset):
        pass

    def setModelParameters(self,modelParameters):
        pass


# 🔹 Repositório específico para Dataset (herda de GenericRepository)
class ModelRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Model)