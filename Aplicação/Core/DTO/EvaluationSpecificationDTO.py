from .DatabaseManager import *
from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class EvaluationSpecificationDTO(Base):
    __tablename__ = 'EvaluationSpecification'

    idEvaluationSpecification = Column(Integer, primary_key=True, autoincrement=True)
    idTask = Column(Integer, ForeignKey('Task.idTask'), nullable=True)
    idEvaluationProcedure = Column(Integer, ForeignKey('EvaluationProcedure.idEvaluationProcedure'), nullable=True)

    tasks = relationship('TaskDTO', back_populates='evaluationSpecification', cascade="all")
    evaluationProcedures =  relationship('EvaluationProcedureDTO', back_populates='evaluationSpecification', cascade="all")

    def __init__(self, idEvaluationSpecification = None):
        self.idEvaluationSpecification = idEvaluationSpecification

  
class EvaluationSpecificationRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, EvaluationSpecificationDTO)