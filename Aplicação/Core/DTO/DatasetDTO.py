from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from ..Relations import Dataset, Feature


class DatasetDTO(Base):
    __tablename__ = 'Dataset' 

    idDataset = Column(Integer, primary_key=True, autoincrement=True)
    targetFeature = Column(String(45), nullable=True)
    name = Column(String(45), nullable=True) 
    tasks = relationship('TaskDTO', back_populates='dataset') 
    features = relationship('FeatureDTO', back_populates='dataset') 

    def __init__(self, targetFeature=None,  idDataset=None, name= None):
        self.idDataset = idDataset
        self.targetFeature = targetFeature 
        self.name = name

    def get_secondary_key(self):
        return 'name'
    
    @property
    def dataset(self):
        params = self.__dict__.copy()
        features = []
        for feature_dto in self.features:
            features.append(Feature(**feature_dto.__dict__))
        params['features'] = features
        return Dataset(**params)


class DatasetRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, DatasetDTO)
 