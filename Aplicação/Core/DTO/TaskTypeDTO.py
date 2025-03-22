from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class TaskTypeDTO(Base):
    __tablename__ = 'TaskType'

    idTaskType = Column(Integer, primary_key=True, autoincrement=True)
    taskType = Column(String(255), nullable=False)
    
    tasks = relationship('TaskDTO', back_populates='taskType')

    def __init__(self, idTaskType= None, taskType= None):
        self.idTaskType = idTaskType
        self.taskType = taskType
 

class TaskTypeRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, TaskTypeDTO)