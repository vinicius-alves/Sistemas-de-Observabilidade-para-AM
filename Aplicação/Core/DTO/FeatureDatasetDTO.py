from .DatabaseManager import *
from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class FeatureDatasetDTO(Base):
    __tablename__ = 'FeatureDataset' 

    idFeatureDataset = Column(Integer, primary_key=True, autoincrement=True) 
    idDataset = Column(Integer, ForeignKey('Dataset.idDataset'), nullable=True) 
    idFeature = Column(Integer, ForeignKey('Feature.idFeature'), nullable=True)

    feature = relationship('FeatureDTO', back_populates='featureDatasets')
    dataset = relationship('DatasetDTO', back_populates='featureDatasets')
   

    def __init__(self,  idFeatureDataset = None, idDataset = None, idFeature = None, feature = None, dataset = None):
        self.idFeatureDataset = idFeatureDataset 
        self.idDataset = idDataset
        self.idFeature = idFeature
        self.feature = feature
        self.dataset = dataset

    def get_secondary_key(self):
        return ['idDataset','idFeature']

class FeatureDatasetRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureDatasetDTO)
 