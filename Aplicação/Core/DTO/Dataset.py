from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship


# 🔹 Modelo genérico de dataset (pode haver outros modelos)
class Dataset(Base):
    __tablename__ = 'dataset'

    idDataset = Column(Integer, primary_key=True)
    targetFeature = Column(String(45), nullable=False)
    data = Column(LargeBinary, nullable=True)  # Armazena grandes volumes de dados binários

    tasks = relationship('Task', back_populates='dataset')
    runs = relationship('Run', back_populates='dataset')

    def __init__(self, idDataset, targetFeature, data=None):
        self.idDataset = idDataset
        self.targetFeature = targetFeature
        self.data = data

# 🔹 Repositório específico (herda de GenericRepository)
class DatasetRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Dataset)
 