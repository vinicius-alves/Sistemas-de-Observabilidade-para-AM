from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Run(Base):
    __tablename__ = 'run'

    idRun = Column(Integer, primary_key=True)
    task = Column(String(255), nullable=False)
    model_id = Column(Integer, ForeignKey('model.idModel'), nullable=False)
    dataset_id = Column(Integer, ForeignKey('dataset.idDataset'), nullable=False)
    parameters = Column(Text, nullable=False)  # Armazena parâmetros como texto JSON ou similar
    results = Column(Text, nullable=True)  # Armazena resultados como texto (pode ser JSON)

    #model = relationship('Model', back_populates='runs')
    #dataset = relationship('Dataset', back_populates='runs')

    def __init__(self, idRun, task, model, dataset, parameters):
        self.idRun = idRun
        self.task = task
        self.model = model
        self.dataset = dataset
        self.parameters = parameters
        self.results = {}

    def execute(self):
        """Executa o processo de treinamento/predição do modelo"""
        pass
        # self.model.train(self.dataset)
        # predictions = self.model.predict(self.dataset)
        # return predictions
    
    def evaluate(self, evaluation_measures):
        """Avalia o modelo com base nas métricas fornecidas"""
        for measure in evaluation_measures:
            self.results[measure.name] = measure.compute(self.dataset, self.model)
        return self.results
    

# 🔹 Repositório específico (herda de GenericRepository)
class RunRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Run)