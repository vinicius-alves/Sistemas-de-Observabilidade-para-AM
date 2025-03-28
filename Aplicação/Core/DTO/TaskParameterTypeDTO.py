from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class TaskParameterTypeDTO(Base):
    __tablename__ = 'TaskParameterType'

    idTaskParameterType = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    
    tasks = relationship('TaskDTO', back_populates='type')

    def __init__(self, idTaskParameterType= None, type= None):
        self.idTaskParameterType = idTaskParameterType
        self.type = type
 

class typeRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, TaskParameterTypeDTO)