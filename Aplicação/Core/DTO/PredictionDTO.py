from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 

class PredictionDTO(Base):
    __tablename__ = 'Prediction' 

    idPrediction = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=True)
    value = Column(String(45), nullable=True)
    type = Column(String(45), nullable=True)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=True)

    run = relationship('RunDTO', back_populates='measures')
     

    def __init__(self, value=None, idPrediction=None, name= None, type = None):
        self.idPrediction = idPrediction
        self.value = value
        self.name = name
        self.type = type


class PredictionRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, PredictionDTO)
 