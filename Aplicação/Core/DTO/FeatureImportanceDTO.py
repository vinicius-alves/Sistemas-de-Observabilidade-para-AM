from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship 


class FeatureImportanceDTO(Base):
    __tablename__ = 'FeatureImportance' 

    idFeatureImportance = Column(Integer, primary_key=True, autoincrement=True)
    importance = Column(Float, nullable=True)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=True)
    idFeature = Column(Integer, ForeignKey('Feature.idFeature'), nullable=True)

    run = relationship('RunDTO', back_populates='featureImportances') 
    feature = relationship('FeatureDTO', back_populates='featureImportances')

    def __init__(self, importance=None, idFeatureImportance=None, idFeature= None, feature = None):
        self.idFeatureImportance = idFeatureImportance
        self.importance = importance
        self.idFeature = idFeature
        self.feature= feature


class FeatureImportanceRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureImportanceDTO)
 