from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Run(Base):
    __tablename__ = 'run'

    idRun = Column(Integer, primary_key=True, autoincrement=True)
    idTask = Column(Integer, ForeignKey('task.idTask'), nullable=True)
    idModel = Column(Integer, ForeignKey('model.idModel'), nullable=True)
     
    measures = relationship('EvaluationMeasure', back_populates='run', cascade="all") 
    model = relationship('Model', back_populates='runs', cascade="all")
    taskParameters = relationship('TaskParameter', back_populates='run', cascade="all")
    task = relationship('Task', back_populates='runs', cascade="all")

    def __init__(self, idTask = None, idModel = None,  idRun = None):
        self.idRun = idRun
        self.idTask = idTask
        self.idModel = idModel

    def execute(self, task, measureProcedures, model, taskParameters):
        self.taskParameters = taskParameters
        self.measures = task.execute(model,  measureProcedures = measureProcedures, taskParameters = taskParameters)
    

class RunRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Run)