from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class SliceDTO(Base):
    __tablename__ = 'Slice'

    idSlice = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(256), nullable=False) 
    condition = Column(String(256), nullable=False) 
    
    subjectSlices = relationship('SubjectSliceDTO', back_populates='slice')

    def __init__(self, idSlice = None, description = None, condition = None):
        self.idSlice = idSlice
        self.description = description
        self.condition = condition

    def get_secondary_key(self):
        return ['description','condition']

class SliceRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, SliceDTO)