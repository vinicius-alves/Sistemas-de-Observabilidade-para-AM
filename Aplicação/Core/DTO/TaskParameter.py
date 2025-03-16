from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class TaskParameter(Base):
    __tablename__ = 'TaskParameter'

    idTaskParameter = Column(Integer, primary_key=True, autoincrement=True)
    nameTaskParameter = Column(String(255), nullable=False)
    valueTaskParameter = Column(Integer, nullable=False)
    idRun = Column(Integer, ForeignKey('run.idRun'), nullable=False)
    run = relationship('Run', back_populates='taskParameters')

    def __init__(self, idTaskParameter = None, nameTaskParameter = None, valueTaskParameter = None):
        self.idTaskParameter = idTaskParameter
        self.nameTaskParameter = nameTaskParameter
        self.valueTaskParameter = valueTaskParameter

class TaskParameterRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, TaskParameter)