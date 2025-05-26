from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class MeasureValueDTO(Base):
    __tablename__ = 'MeasureValue'

    idMeasureValue = Column(Integer, primary_key=True, autoincrement=True)
    
    value = Column(Float, nullable=True)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=True)
    idEvaluationProcedure = Column(Integer, ForeignKey('EvaluationProcedure.idEvaluationProcedure'), nullable=True)
    idMeasure = Column(Integer, ForeignKey('Measure.idMeasure'), nullable=True)


    measure = relationship('MeasureDTO', back_populates='measureValues')
    run = relationship('RunDTO', back_populates='measureValues')
    evaluationProcedure = relationship('EvaluationProcedureDTO', back_populates='measureValues')

    def __init__(self, value = None, idMeasureValue = None):
        self.idMeasureValue = idMeasureValue
        self.value = value

class MeasureValueRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, MeasureValueDTO)