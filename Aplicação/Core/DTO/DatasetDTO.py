from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
import io
import pandas as pd
from ..Relations import Dataset

class DatasetDTO(Base):
    __tablename__ = 'dataset' 

    idDataset = Column(Integer, primary_key=True, autoincrement=True)
    targetFeature = Column(String(45), nullable=False)
    data = Column(LargeBinary, nullable=True)
    tasks = relationship('TaskDTO', back_populates='dataset') 

    def __init__(self, targetFeature, data=None, df=None, idDataset=None):
        self.idDataset = idDataset
        self.targetFeature = targetFeature
        self.data = data
        self.df = df

    def df_to_data(self):
        if self.df is not None:
            buffer = io.BytesIO()
            self.df.to_parquet(buffer, engine='pyarrow')
            self.data = buffer.getvalue()

    def data_to_df(self):
        if self.data is not None:
            buffer = io.BytesIO(self.data)
            self.df = pd.read_parquet(buffer, engine='pyarrow')

    @property
    def dataset(self):
        return Dataset(**self.__dict__)

    @property
    def df(self):
        return self.__dict__["df"]

    @df.setter
    def df(self, novo_valor):
        self.__dict__["df"] = novo_valor
        self.df_to_data()

    '''
    @property
    def data(self):
        return self.__dict__["data"]'
    

    @data.setter
    def data(self, novo_valor):
        if novo_valor != self.__dict__.get("data", None):
            self.__dict__["data"] = novo_valor
            self.data_to_df() 
    '''


class DatasetRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, DatasetDTO)
 