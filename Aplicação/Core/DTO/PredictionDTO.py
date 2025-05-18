from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship 

class PredictionDTO(Base):
    __tablename__ = 'Prediction' 

    idPrediction = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(45), nullable=True)
    type = Column(String(45), nullable=True)
    timestamp = Column(DateTime, nullable=True)
    idEntity = Column(String(45), nullable=True)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=True)

    run = relationship('RunDTO', back_populates='predictions')
    predictionFeatureContributions = relationship('PredictionFeatureContributionDTO', back_populates='prediction')
    

    def __init__(self, value=None, idPrediction=None, type = None, idEntity = None):
        self.idPrediction = idPrediction
        self.value = value
        self.type = type
        self.idEntity = idEntity


class PredictionRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, PredictionDTO)