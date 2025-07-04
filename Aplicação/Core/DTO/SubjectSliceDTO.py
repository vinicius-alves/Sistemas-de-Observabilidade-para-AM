from .DatabaseManager import *
from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class SubjectSliceDTO(Base):
    __tablename__ = 'SubjectSlice'

    idSubjectSlice = Column(Integer, primary_key=True, autoincrement=True)
    idMeasure = Column(Integer, ForeignKey('Measure.idMeasure'), nullable=True)
    idSlice = Column(Integer, ForeignKey('Slice.idSlice'), nullable=True)

    measure = relationship('MeasureDTO', back_populates='subjectSlices', cascade="all")
    slice = relationship('SliceDTO', back_populates='subjectSlices', cascade="all")

    def __init__(self,  idSubjectSlice = None, measure = None, slice = None):
        self.idSubjectSlice = idSubjectSlice
        self.measure = measure
        self.slice = slice

    def get_secondary_key(self):
        return ['idMeasure','idSlice']

class SubjectSliceRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, SubjectSliceDTO)