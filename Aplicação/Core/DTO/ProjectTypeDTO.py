from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class ProjectTypeDTO(Base):
    __tablename__ = 'ProjectType'

    idProjectType = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    projects = relationship('ProjectDTO', back_populates='projectType')

    def __init__(self, idProjectType = None, name = None):
        self.idProjectType = idProjectType
        self.name = name 

class ProjectTypeRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, ProjectTypeDTO)