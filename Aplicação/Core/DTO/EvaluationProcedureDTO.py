from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, LargeBinary

class ProcedureDTO(Base):
    __tablename__ = 'EvaluationProcedure'

    idEvluationProcedure = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    object = Column(LargeBinary, nullable=True)

    def __init__(self, name, object = None, idEvluationProcedure = None):
        self.idEvluationProcedure = idEvluationProcedure
        self.name = name
        self.object = object
  
class MeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, ProcedureDTO)