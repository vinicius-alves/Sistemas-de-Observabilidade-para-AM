from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class TaskParameter(Base):
    __tablename__ = 'TaskParameter'

    idTaskParameter = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    value = Column(Integer, nullable=False)
    idRun = Column(Integer, ForeignKey('run.idRun'), nullable=False)
    run = relationship('Run', back_populates='taskParameters')

    def __init__(self, idTaskParameter = None, name = None, value = None):
        self.idTaskParameter = idTaskParameter
        self.name = name
        self.value = value

class TaskParameterRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, TaskParameter)