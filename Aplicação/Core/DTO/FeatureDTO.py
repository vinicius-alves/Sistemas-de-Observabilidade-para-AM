from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class FeatureDTO(Base):
    __tablename__ = 'Feature' 

    idFeature = Column(Integer, primary_key=True, autoincrement=True) 
    idDataset = Column(Integer, ForeignKey('Dataset.idDataset'), nullable=True) 
    name = Column(String(45), nullable=True) 
    nameSpace = Column(String(45), nullable=True)  


    dataset = relationship('DatasetDTO', back_populates='features') 

    def __init__(self,  idFeature = None, name = None, nameSpace = None):
        self.idFeature = idFeature 
        self.name = name
        self.nameSpace = nameSpace


class FeatureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureDTO)
 