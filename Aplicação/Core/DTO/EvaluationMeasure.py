from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String

class EvaluationMeasure(Base):
    __tablename__ = 'evaluationmeasure'

    idMeasure = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(1000), nullable=True)
    measureValue = Column(Integer, nullable=False)

    def __init__(self, measureValue, description, idMeasure = None):
        self.idMeasure = idMeasure
        self.measureValue = measureValue
        self.description = description

# 🔹 Repositório específico (herda de GenericRepository)
class EvaluationMeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, EvaluationMeasure)