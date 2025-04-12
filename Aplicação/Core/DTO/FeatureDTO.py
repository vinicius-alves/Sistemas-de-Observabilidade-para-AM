from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship 


class FeatureDTO(Base):
    __tablename__ = 'Feature' 

    idFeature = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=True)
    value = Column(String(45), nullable=True)
    type = Column(String(45), nullable=True)
    timestamp = Column(DateTime, nullable=True)
    idDataset = Column(Integer, ForeignKey('Dataset.idDataset'), nullable=True)
    dataset = relationship('DatasetDTO', back_populates='features') 

    def __init__(self, value=None, idFeature=None, name= None, type = None):
        self.idFeature = idFeature
        self.value = value
        self.name = name
        self.type = type


class FeatureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureDTO)
 