from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 


class FeatureImportanceDTO(Base):
    __tablename__ = 'FeatureImportance' 

    idFeatureImportance = Column(Integer, primary_key=True, autoincrement=True)
    feature = Column(String(45), nullable=True)
    featureNameSpace = Column(String(45), nullable=True)
    importance = Column(String(45), nullable=True)

    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=True)
    run = relationship('RunDTO', back_populates='featureImportances') 

    def __init__(self, importance=None, idFeatureImportance=None, feature= None, featureNameSpace = None):
        self.idFeatureImportance = idFeatureImportance
        self.importance = importance
        self.feature = feature
        self.featureNameSpace = featureNameSpace


class FeatureImportanceRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureImportanceDTO)
 