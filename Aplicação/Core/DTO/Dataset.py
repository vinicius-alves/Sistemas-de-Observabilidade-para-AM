from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
import io
import pandas as pd


# 🔹 Modelo genérico de dataset (pode haver outros modelos)
class Dataset(Base):
    __tablename__ = 'dataset'

    idDataset = Column(Integer, primary_key=True, autoincrement=True)
    targetFeature = Column(String(45), nullable=False)
    data = Column(LargeBinary, nullable=True)  # Armazena grandes volumes de dados binários
    tasks = relationship('Task', back_populates='dataset')

    def __init__(self, targetFeature, data=None, df = None, idDataset=None):
        self.idDataset = idDataset
        self.targetFeature = targetFeature
        self.data = data
        self.df = df
        if df is not None and data is None:
            self.df_to_data()
        if data is not None and df is None:
            self.data_to_df()

    def df_to_data(self):
        buffer = io.BytesIO()
        self.df.to_parquet(buffer, engine='pyarrow')
        self.data= buffer.getvalue()
    
    def data_to_df(self):
        buffer = io.BytesIO(self.data)  
        self.df = pd.read_parquet(buffer, engine='pyarrow')

# 🔹 Repositório específico (herda de GenericRepository)
class DatasetRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, Dataset)
 