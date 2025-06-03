from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class SubjectMeasureDTO(Base):
    __tablename__ = 'SubjectMeasure'

    idSubjectMeasure = Column(Integer, primary_key=True, autoincrement=True)
    idMeasure = Column(Integer, ForeignKey('Measure.idMeasure'), nullable=True)
    idReferenceMeasure = Column(Integer, ForeignKey('Measure.idMeasure'), nullable=True)

    measure = relationship('MeasureDTO', back_populates='subjectMeasures', cascade="all", foreign_keys=[idMeasure])
    referenceMeasure = relationship('MeasureDTO', back_populates='subjectReferenceMeasures', cascade="all", foreign_keys=[idReferenceMeasure])

    def __init__(self,  idSubjectMeasure = None, measure = None, referenceMeasure = None):
        self.idSubjectMeasure = idSubjectMeasure
        self.measure = measure
        self.referenceMeasure = referenceMeasure

    def get_secondary_key(self):
        return ['idMeasure','idReferenceMeasure']

class SubjectMeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, SubjectMeasureDTO)