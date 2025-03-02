from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

class Model(Base):
    __tablename__ = 'model'

    idModel = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    version = Column(String(50), nullable=False)
    description = Column(String(1000), nullable=True)

    runs = relationship('Run', back_populates='model')

    def __init__(self, idModel, name, version, description):
        self.idModel = idModel
        self.name = name
        self.version = version
        self.description = description


# 🔹 Repositório específico para Dataset (herda de GenericRepository)
class ModelRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Model)