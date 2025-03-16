from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = 'task'

    idTask = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    idTaskType = Column(Integer, ForeignKey('tasktype.idTaskType'), nullable=False)
    idDataset = Column(Integer, ForeignKey('dataset.idDataset'), nullable=False)

    dataset = relationship('Dataset', back_populates='tasks', cascade="all")
    taskType = relationship('TaskType', back_populates='tasks', cascade="all")
    runs = relationship('Run', back_populates='task')

    def __init__(self, name= None, idTaskType= None, dataset= None, idTask = None):
        self.idTask = idTask
        self.name = name
        self.idTaskType = idTaskType
        self.dataset = dataset

    def execute(self, model, parameters):
        raise NotImplementedError('Base class method')
    

class TaskRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Task)