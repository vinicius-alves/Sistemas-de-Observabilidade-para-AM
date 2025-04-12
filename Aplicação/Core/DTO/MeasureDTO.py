from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class MeasureDTO(Base):
    __tablename__ = 'Measure'

    idMeasure = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(1000), nullable=True)
    value = Column(Float, nullable=True)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=True)
    idEvaluationProcedure = Column(Integer, ForeignKey('EvaluationProcedure.idEvaluationProcedure'), nullable=True)

    run = relationship('RunDTO', back_populates='measures')
    evaluationProcedure = relationship('EvaluationProcedureDTO', back_populates='measures')

    def __init__(self, value = None, name = None, idMeasure = None):
        self.idMeasure = idMeasure
        self.value = value
        self.name = name

class MeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, MeasureDTO)