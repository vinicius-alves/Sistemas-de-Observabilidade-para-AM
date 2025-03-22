from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class TaskParameterDTO(Base):
    __tablename__ = 'TaskParameter'

    idTaskParameter = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    value = Column(Integer, nullable=False)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=False)
    run = relationship('RunDTO', back_populates='taskParameters')

    def __init__(self, idTaskParameter = None, name = None, value = None):
        self.idTaskParameter = idTaskParameter
        self.name = name
        self.value = value

class TaskParameterRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, TaskParameterDTO)