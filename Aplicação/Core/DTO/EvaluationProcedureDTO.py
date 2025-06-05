from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship

class EvaluationProcedureDTO(Base):
    __tablename__ = 'EvaluationProcedure'

    idEvaluationProcedure = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    measureValues = relationship('MeasureValueDTO', back_populates='evaluationProcedure', cascade="all") 

    def __init__(self, name= None,  idEvaluationProcedure = None):
        self.idEvaluationProcedure = idEvaluationProcedure
        self.name = name

    def get_secondary_key(self):
        return ['name']
  
class EvaluationProcedureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, EvaluationProcedureDTO)