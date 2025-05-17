from .DatabaseManager import *
from sqlalchemy import  Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship 


class PredictionFeatureContributionDTO(Base):
    __tablename__ = 'PredictionFeatureContribution' 

    idPredictionFeatureContribution = Column(Integer, primary_key=True, autoincrement=True)
    contribution = Column(Float, nullable=True)
    idPrediction = Column(Integer, ForeignKey('Prediction.idPrediction'), nullable=True)
    idFeature = Column(Integer, ForeignKey('Feature.idFeature'), nullable=True)

    prediction = relationship('PredictionDTO', back_populates='predictionFeatureContributions') 
    feature = relationship('FeatureDTO', back_populates='predictionFeatureContributions')

    def __init__(self, contribution=None, idPredictionFeatureContribution=None, idFeature= None, feature = None):
        self.idPredictionFeatureContribution = idPredictionFeatureContribution
        self.contribution = contribution
        self.idFeature = idFeature
        self.feature= feature


class PredictionFeatureContributionRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, PredictionFeatureContributionDTO)
 