from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class FeatureNameSpaceDTO(Base):
    __tablename__ = 'FeatureNameSpace' 

    idFeatureNameSpace = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String(256), nullable=True)  

    features = relationship('FeatureDTO', back_populates='nameSpace')

    def __init__(self,  idFeatureNameSpace = None, name = None):
        self.idFeatureNameSpace = idFeatureNameSpace 
        self.name = name

    def get_secondary_key(self):
        return ['name']


class FeatureNameSpaceRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, FeatureNameSpaceDTO)
 