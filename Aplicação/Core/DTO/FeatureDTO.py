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

    def __init__(self, **kwargs):
        self.idFeature = kwargs.get("idFeature", None) 
        self.value = kwargs.get("value", None)
        self.name = kwargs.get("name", None)
        self.type = kwargs.get("type", None)
        self.timestamp = kwargs.get("timestamp", None)


class FeatureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureDTO)
 