from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class SubjectFeatureDTO(Base):
    __tablename__ = 'SubjectFeature'

    idSubjectFeature = Column(Integer, primary_key=True, autoincrement=True)
    idMeasure = Column(Integer, ForeignKey('Measure.idMeasure'), nullable=True)
    idFeature = Column(Integer, ForeignKey('Feature.idFeature'), nullable=True)

    measure = relationship('MeasureDTO', back_populates='subjectFeatures', cascade="all")
    feature = relationship('FeatureDTO', back_populates='subjectFeatures', cascade="all")

    def __init__(self,  idSubjectFeature = None, measure = None, feature = None):
        self.idSubjectFeature = idSubjectFeature
        self.measure = measure
        self.feature = feature

    def get_secondary_key(self):
        return ['idMeasure','idFeature']

class SubjectFeatureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, SubjectFeatureDTO)