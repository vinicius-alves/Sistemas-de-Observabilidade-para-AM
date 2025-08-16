from .DatabaseManager import *
from sqlalchemy import  Column, Integer, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class RunDTO(Base):
    __tablename__ = 'Run'

    idRun = Column(Integer, primary_key=True, autoincrement=True)
    idTask = Column(Integer, ForeignKey('Task.idTask'), nullable=True)
    idModel = Column(Integer, ForeignKey('Model.idModel'), nullable=True)
    idProject = Column(Integer, ForeignKey('Project.idProject'), nullable=True)
    createdTimestamp = Column(DateTime, default=datetime.now())  
    idDataset = Column(Integer, ForeignKey('Dataset.idDataset'), nullable=True)  

    dataset = relationship('DatasetDTO', back_populates='runs', cascade="all")  
    measureValues = relationship('MeasureValueDTO', back_populates='run', cascade="all") 
    model = relationship('ModelDTO', back_populates='runs', cascade="all") 
    project = relationship('ProjectDTO', back_populates='runs', cascade="all") 
    parameters = relationship('ParameterDTO', back_populates='run', cascade="all")
    predictions = relationship('PredictionDTO', back_populates='run', cascade="all") 
    task = relationship('TaskDTO', back_populates='runs', cascade="all")
    featureImportances = relationship('FeatureImportanceDTO', back_populates='run')

    def __init__(self, idTask = None, dataset= None, idModel = None,  idRun = None):
        self.idRun = idRun
        self.idTask = idTask
        self.idModel = idModel
        self.dataset = dataset

    

class RunRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, RunDTO)