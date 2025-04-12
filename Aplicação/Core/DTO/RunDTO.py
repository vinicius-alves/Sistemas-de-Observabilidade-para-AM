from .DatabaseManager import *
from sqlalchemy import  Column, Integer, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class RunDTO(Base):
    __tablename__ = 'Run'

    idRun = Column(Integer, primary_key=True, autoincrement=True)
    idTask = Column(Integer, ForeignKey('Task.idTask'), nullable=True)
    idModel = Column(Integer, ForeignKey('Model.idModel'), nullable=True)
    createdTimestamp = Column(DateTime, default=datetime.now())  
     
    measures = relationship('MeasureDTO', back_populates='run', cascade="all") 
    predictions = relationship('PredictionDTO', back_populates='run', cascade="all") 
    model = relationship('ModelDTO', back_populates='runs', cascade="all") 
    parameters = relationship('ParameterDTO', back_populates='run', cascade="all")
    task = relationship('TaskDTO', back_populates='runs', cascade="all")

    def __init__(self, idTask = None, idModel = None,  idRun = None):
        self.idRun = idRun
        self.idTask = idTask
        self.idModel = idModel

    

class RunRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, RunDTO)