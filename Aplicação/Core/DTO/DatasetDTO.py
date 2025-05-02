from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..Relations import Dataset
import pandas as pd
from .FeatureDTO import FeatureDTO
from .FeatureNameSpaceDTO import FeatureNameSpaceDTO


class DatasetDTO(Base):
    __tablename__ = 'Dataset' 

    idDataset = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=True) 
    startTimestamp = Column(DateTime, nullable=True) 
    endTimestamp = Column(DateTime, nullable=True) 
    tasks = relationship('TaskDTO', back_populates='dataset') 
    features = relationship('FeatureDTO', back_populates='dataset')

    def __init__(self,  idDataset=None, name= None, instructions = None):
        self.idDataset = idDataset
        self.name = name
        self.instructions = instructions

    def get_secondary_key(self):
        return ['name']
    
    def save_data_mongo(self,mongo_db ,df, nameSpace):
        mycol = mongo_db["feature"] 
        mycol.delete_many({'nameSpace':nameSpace})
        lst_records = df.to_dict(orient = 'records')

        lst_features = df['name'].drop_duplicates().to_list()
        nameSpaceDTO =  FeatureNameSpaceDTO(name = nameSpace)
        for feature in lst_features:
            self.features.append(FeatureDTO(name = feature, nameSpace=nameSpaceDTO))

        return mycol.insert_many(lst_records)
    
    def load_data_from_mongo(self, mongo_db):

        if len(self.features) == 0:
            return
        
        filter_dic = {'$or': []}

        for feature in self.features:
            filter_dic['$or'].append({'name': feature.name, 'nameSpace':feature.nameSpace.name})

        if self.startTimestamp or self.endTimestamp:
            filter_dic['timestamp'] = {}

            if self.startTimestamp:
                filter_dic['timestamp']['$gt'] = "ISODate(\'"+str(self.startTimestamp)+  "\')"

            if self.endTimestamp:
                filter_dic['timestamp']['$lte'] = "ISODate(\'"+str(self.endTimestamp)+  "\')"

        df = pd.DataFrame(list(mongo_db['feature'].find(filter_dic))).drop(columns = '_id')
        df['value'] = df.apply(lambda x : eval(x['type'])(x['value'])  ,axis = 1)
        df['name'] = df['nameSpace']+ '__'+ df['name']
        df.drop(columns = ['nameSpace'], inplace=True)
        df_data = df.pivot_table(index = ['timestamp'], values= ['value'], columns= ['name'], aggfunc='max')
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
 