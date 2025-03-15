from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Run import Run

class Task(Base):
    __tablename__ = 'task'

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    task_type = Column(String(50), nullable=False)
    dataset_id = Column(Integer, ForeignKey('dataset.idDataset'), nullable=False)
    time_frame = Column(String(50), nullable=True)

    dataset = relationship('Dataset', back_populates='tasks')

    def __init__(self, name, task_type, dataset, time_frame, idTask = None):
        self.idTask = idTask
        self.name = name
        self.task_type = task_type
        self.dataset = dataset
        self.time_frame = time_frame

    def execute(self, model, parameters):
        """Executa a tarefa e cria um Run"""
        #return Run(run_id=1, task=self, model=model, dataset=self.dataset, parameters=parameters)
        pass
    

# 🔹 Repositório específico (herda de GenericRepository)
class TaskRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Task)