from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String

class EvaluationMeasure(Base):
    __tablename__ = 'evaluationmeasure'

    idMeasure = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)

    def __init__(self, name, description, idMeasure = None):
        self.idMeasure = idMeasure
        self.name = name
        self.description = description

    def compute(self, dataset, model):
        """Método de cálculo que pode ser implementado conforme necessidade."""
        pass

# 🔹 Repositório específico (herda de GenericRepository)
class EvaluationMeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, EvaluationMeasure)