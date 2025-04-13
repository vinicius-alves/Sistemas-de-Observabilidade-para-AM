from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from ..Relations import Dataset
import pandas as pd


class DatasetDTO(Base):
    __tablename__ = 'Dataset' 

    idDataset = Column(Integer, primary_key=True, autoincrement=True)
    targetFeature = Column(String(45), nullable=True)
    name = Column(String(45), nullable=True) 
    instructions = Column(JSON, nullable=True) 
    tasks = relationship('TaskDTO', back_populates='dataset') 

    def __init__(self, targetFeature=None,  idDataset=None, name= None, instructions = None):
        self.idDataset = idDataset
        self.targetFeature = targetFeature 
        self.name = name
        self.instructions = instructions

    def get_secondary_key(self):
        return 'name'
    
    def save_data_mongo(self,mongo_db ,df):
        mycol = mongo_db["feature"]
        lst_records = df.to_dict(orient = 'records')
        return mycol.insert_many(lst_records)
    
    def load_data_from_mongo(self, mongo_db):
        if self.instructions is not None:
            df = pd.DataFrame(list(mongo_db['feature'].find(self.instructions))).drop(columns = '_id')
            df['value'] = df.apply(lambda x : eval(x['type'])(x['value'])  ,axis = 1)
            df_data = df.pivot_table(index = ['timestamp','prediction'], values= ['value'], columns= ['name'], aggfunc='max')
            df_data.columns = [i[1] for i in df_data.columns]
            df_data = df_data.reset_index()
            self.df = pd.DataFrame(df_data.to_dict())
    
    @property
    def dataset(self):
        params = self.__dict__.copy()
        return Dataset(**params)


class DatasetRepository(GenericRepository):
    def __init__(self, session):
        super().__init__(session, DatasetDTO)
 