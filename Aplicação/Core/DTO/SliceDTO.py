from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class SliceDTO(Base):
    __tablename__ = 'Slice'

    idSlice = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(256), nullable=False) 
    condition = Column(String(256), nullable=False) 
    idFeature = Column(Integer, ForeignKey('Feature.idFeature'), nullable=False)

    feature = relationship('FeatureDTO', back_populates='slices')
    subjectSlices = relationship('SubjectSliceDTO', back_populates='slice')

    def __init__(self, idSlice = None, description = None, condition = None, idFeature = None, projectType= None, feature = None):
        self.idSlice = idSlice
        self.description = description
        self.condition = condition
        self.idFeature = idFeature 
        self.feature = feature

    def get_secondary_key(self):
        return ['idFeature','condition']

class SliceRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, SliceDTO)