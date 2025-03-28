from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ModelParameterDTO(Base):
    __tablename__ = 'ModelParameter'

    idModelParameter = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=False)
    run = relationship('RunDTO', back_populates='modelParameters')

    def __init__(self, idModelParameter = None, name = None, value = None):
        self.idModelParameter = idModelParameter
        self.name = name
        self.value = value

class ModelParameterRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, ModelParameterDTO)