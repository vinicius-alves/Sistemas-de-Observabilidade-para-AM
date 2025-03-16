from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class EvaluationMeasure(Base):
    __tablename__ = 'evaluationmeasure'

    idMeasure = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(1000), nullable=True)
    measureValue = Column(Integer, nullable=False)
    idRun = Column(Integer, ForeignKey('run.idRun'), nullable=True)

    run = relationship('Run', back_populates='measures')

    def __init__(self, measureValue, name, idMeasure = None):
        self.idMeasure = idMeasure
        self.measureValue = measureValue
        self.name = name

class EvaluationMeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, EvaluationMeasure)