from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from .SubjectMeasureDTO import SubjectMeasureDTO

class MeasureDTO(Base):
    __tablename__ = 'Measure'

    idMeasure = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    measureValues = relationship('MeasureValueDTO', back_populates='measure')


    subjectMeasures = relationship('SubjectMeasureDTO', back_populates='measure',
    foreign_keys=lambda : [SubjectMeasureDTO.idMeasure])
    subjectReferenceMeasures = relationship('SubjectMeasureDTO', back_populates='referenceMeasure',
    foreign_keys=lambda : [SubjectMeasureDTO.idReferenceMeasure])
    subjectFeatures = relationship('SubjectFeatureDTO', back_populates='measure')
    subjectSlices = relationship('SubjectSliceDTO', back_populates='measure')
    subjectEntities = relationship('SubjectEntityDTO', back_populates='measure')

    def __init__(self,  name = None, idMeasure = None):
        self.idMeasure = idMeasure
        self.name = name

  
class MeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, MeasureDTO)