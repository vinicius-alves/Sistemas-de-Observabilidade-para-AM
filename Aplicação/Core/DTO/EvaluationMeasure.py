from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class EvaluationMeasure(Base):
    __tablename__ = 'evaluationmeasure'

    idMeasure = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(1000), nullable=True)
    measureValue = Column(Integer, nullable=False)
    idRun = Column(Integer, ForeignKey('run.idRun'), nullable=True)

    run = relationship('Run', back_populates='measures')

    def __init__(self, measureValue, description, idMeasure = None):
        self.idMeasure = idMeasure
        self.measureValue = measureValue
        self.description = description

    def evaluate(self, **kwargs):
        raise NotImplementedError('Base class method')

class EvaluationMeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, EvaluationMeasure)