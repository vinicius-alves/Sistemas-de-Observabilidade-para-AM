from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class TaskTypeDTO(Base):
    __tablename__ = 'TaskType'

    idTaskType = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(256), nullable=True)
    
    tasks = relationship('TaskDTO', back_populates='taskType')

    def __init__(self, idTaskType= None, type= None):
        self.idTaskType = idTaskType
        self.type = type
 

class TaskTypeRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, TaskTypeDTO)