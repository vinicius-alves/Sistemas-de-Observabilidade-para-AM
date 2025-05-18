from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class FeatureDTO(Base):
    __tablename__ = 'Feature' 

    idFeature = Column(Integer, primary_key=True, autoincrement=True) 
    idFeatureNameSpace = Column(Integer, ForeignKey('FeatureNameSpace.idFeatureNameSpace'), nullable=True)
    name = Column(String(45), nullable=True) 

    nameSpace = relationship('FeatureNameSpaceDTO', back_populates='features') 
    projects = relationship('ProjectDTO', back_populates='targetFeature')
    featureImportances = relationship('FeatureImportanceDTO', back_populates='feature')
    featureDatasets = relationship('FeatureDatasetDTO', back_populates='feature')
    predictionFeatureContributions = relationship('PredictionFeatureContributionDTO', back_populates='feature')

    def __init__(self,  idFeature = None, name = None, nameSpace = None):
        self.idFeature = idFeature 
        self.name = name
        self.nameSpace = nameSpace

    def get_secondary_key(self):
        return ['idFeatureNameSpace','name']
    
    def get_full_name(self):
        #return str(self.nameSpace.name) +'__'+self.name
        return self.name


class FeatureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureDTO)
 