from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class ParameterTypeDTO(Base):
    __tablename__ = 'ParameterType'

    idParameterType = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    parameters = relationship('ParameterDTO', back_populates='parameterType')

    def __init__(self, idParameterType = None, name = None):
        self.idParameterType = idParameterType
        self.name = name 

class ParameterTypeRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, ParameterTypeDTO)