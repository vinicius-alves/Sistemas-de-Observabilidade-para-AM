from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class MeasureDTO(Base):
    __tablename__ = 'Measure'

    idMeasure = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(1000), nullable=True)
    measureValues = relationship('MeasureValueDTO', back_populates='measure')

    def __init__(self,  name = None, idMeasure = None):
        self.idMeasure = idMeasure
        self.name = name

    def get_secondary_key(self):
        return ['name']

class MeasureRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, MeasureDTO)