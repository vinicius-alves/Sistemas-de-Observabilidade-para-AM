from .DatabaseManager import *
from sqlalchemy import  Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

class SubjectEntityDTO(Base):
    __tablename__ = 'SubjectEntity'

    idSubjectEntity = Column(Integer, primary_key=True, autoincrement=True)
    idMeasure = Column(Integer, ForeignKey('Measure.idMeasure'), nullable=True)
    idEntity = Column(String(256), nullable=True)
    timestamp = Column(DateTime, nullable=True)
    measure = relationship('MeasureDTO', back_populates='subjectEntities', cascade="all")
     

    def __init__(self,  idSubjectEntity = None, measure = None, idEntity = None, timestamp = None):
        self.idSubjectEntity = idSubjectEntity
        self.measure = measure
        self.idEntity = idEntity
        self.timestamp = timestamp

    def get_secondary_key(self):
        return ['idMeasure','idEntity','timestamp']

class SubjectEntityRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, SubjectEntityDTO)