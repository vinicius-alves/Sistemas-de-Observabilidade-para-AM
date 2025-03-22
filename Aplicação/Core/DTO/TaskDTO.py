from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class TaskDTO(Base):
    __tablename__ = 'Task'

    idTask = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    idTaskType = Column(Integer, ForeignKey('TaskType.idTaskType'), nullable=False)
    idDataset = Column(Integer, ForeignKey('dataset.idDataset'), nullable=False)  

    dataset = relationship('DatasetDTO', back_populates='tasks', cascade="all")  
    taskType = relationship('TaskTypeDTO', back_populates='tasks', cascade="all")
    runs = relationship('RunDTO', back_populates='task')

    def __init__(self, name=None, idTaskType=None, idDataset=None, idTask=None):
        self.idTask = idTask
        self.name = name
        self.idTaskType = idTaskType
        self.idDataset = idDataset

    def execute(self, ModelDTO, parameters):
        raise NotImplementedError('Base class method')
    

class TaskRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, TaskDTO)