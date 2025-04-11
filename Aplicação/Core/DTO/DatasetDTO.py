from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from ..Relations import Dataset


class DatasetDTO(Base):
    __tablename__ = 'dataset' 

    idDataset = Column(Integer, primary_key=True, autoincrement=True)
    targetFeature = Column(String(45), nullable=True)
    name = Column(String(45), nullable=True)
    data = Column(LargeBinary, nullable=True)
    tasks = relationship('TaskDTO', back_populates='dataset') 

    def __init__(self, targetFeature=None, data=None, idDataset=None, name= None, dataset = None):
        self.idDataset = idDataset
        self.targetFeature = targetFeature
        self.data = data
        self.name = name

        if dataset is not None:
            self.targetFeature = dataset.targetFeature
            self.data = dataset.data
            self.name = dataset.name

    def get_secondary_key(self):
        return 'name'
    
    @property
    def dataset(self):
        return Dataset(**self.__dict__)


class DatasetRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, DatasetDTO)
 