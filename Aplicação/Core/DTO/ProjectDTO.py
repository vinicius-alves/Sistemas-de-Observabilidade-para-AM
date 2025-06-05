from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ProjectDTO(Base):
    __tablename__ = 'Project'

    idProject = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False) 
    idProjectType = Column(Integer, ForeignKey('ProjectType.idProjectType'), nullable=False)
    idTargetFeature = Column(Integer, ForeignKey('Feature.idFeature'), nullable=False)

    runs = relationship('RunDTO', back_populates='project')
    projectType = relationship('ProjectTypeDTO', back_populates='projects')
    targetFeature = relationship('FeatureDTO', back_populates='projects')

    def __init__(self, idProject = None, name = None, idTargetFeature = None, projectType= None, targetFeature = None):
        self.idProject = idProject
        self.name = name
        self.idTargetFeature = idTargetFeature
        self.projectType = projectType
        self.targetFeature = targetFeature

    def get_secondary_key(self):
        return ['name']

class ProjectRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, ProjectDTO)