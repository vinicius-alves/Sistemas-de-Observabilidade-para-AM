from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ParameterDTO(Base):
    __tablename__ = 'Parameter'

    idParameter = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    value = Column(String(16000), nullable=False)
    valueType = Column(String(256), nullable=False)
    idRun = Column(Integer, ForeignKey('Run.idRun'), nullable=False)
    idParameterType = Column(Integer, ForeignKey('ParameterType.idParameterType'), nullable=False)

    run = relationship('RunDTO', back_populates='parameters')
    parameterType = relationship('ParameterTypeDTO', back_populates='parameters')

    def __init__(self, idParameter = None, name = None, value = None):
        self.idParameter = idParameter
        self.name = name
        self.value = value

class ParameterRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, ParameterDTO)