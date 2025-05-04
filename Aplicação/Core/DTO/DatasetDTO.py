from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..Relations import Dataset
import pandas as pd
from .FeatureDTO import FeatureDTO
from .FeatureDatasetDTO import FeatureDatasetDTO
from .FeatureNameSpaceDTO import FeatureNameSpaceDTO


class DatasetDTO(Base):
    __tablename__ = 'Dataset' 

    idDataset = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=True) 
    startTimestamp = Column(DateTime, nullable=True) 
    endTimestamp = Column(DateTime, nullable=True) 
    tasks = relationship('TaskDTO', back_populates='dataset') 
    featureDatasets = relationship('FeatureDatasetDTO', back_populates='dataset')

    def __init__(self,  idDataset=None, name= None, instructions = None):
        self.idDataset = idDataset
        self.name = name
        self.instructions = instructions

    def get_secondary_key(self):
        return ['name']
    
    def process_feature_list(self, lst_features, name_space):
        name_space_obj =  FeatureNameSpaceDTO(name = name_space)
        for feature in lst_features:
            featureDatasetDTO =FeatureDatasetDTO()
            featureDatasetDTO.feature = FeatureDTO(name = feature, nameSpace=name_space_obj)
            self.featureDatasets.append(featureDatasetDTO)

    def save_data_mongo(self,mongo_db ,df):
        mycol = mongo_db["featurevalue"] 
        filter_dic = self.get_mongo_query()
        mycol.delete_many(filter_dic)

        feature_map = {}
        for feature in self.get_all_features():
            feature_map[feature.name] = feature.idFeature
        
        df['idFeature'] = df['name'].map(lambda x : feature_map[x])
        df.drop(columns = ['name'], inplace = True)
        lst_records = df.to_dict(orient = 'records')
        return mycol.insert_many(lst_records)
    

    def get_all_features(self):
        features = []
        if len(self.featureDatasets) == 0:
            return features
        for featureDataset in self.featureDatasets:
            features.append(featureDataset.feature)
        return features
    
    def get_feature_by_name(self, name):
        for feature in self.get_all_features():
            if feature.name == name:
                return feature
    

    def get_mongo_query(self):
        if len(self.featureDatasets) == 0:
            return
        
        filter_dic = {'$or': []}

        features = self.get_all_features()
        for feature in features:
            filter_dic['$or'].append({'idFeature':feature.idFeature})

        if self.startTimestamp or self.endTimestamp:
            filter_dic['timestamp'] = {}

            if self.startTimestamp:
                filter_dic['timestamp']['$gt'] = "ISODate(\'"+str(self.startTimestamp)+  "\')"

            if self.endTimestamp:
                filter_dic['timestamp']['$lte'] = "ISODate(\'"+str(self.endTimestamp)+  "\')"

        return filter_dic
    
    def load_data_from_mongo(self, mongo_db):

        filter_dic = self.get_mongo_query()
        df = pd.DataFrame(list(mongo_db['featurevalue'].find(filter_dic))).drop(columns = '_id')
        df['value'] = df.apply(lambda x : eval(x['type'])(x['value'])  ,axis = 1)

        feature_map = {}
        for feature in self.get_all_features():
            feature_map[feature.idFeature] = feature.get_full_name()

        df['name'] = df['idFeature'].map(lambda x : feature_map[x])  
        df.drop(columns = ['idFeature'], inplace = True)  

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
 