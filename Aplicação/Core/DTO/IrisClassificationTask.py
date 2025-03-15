from .DatabaseManager import *
from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Task import Task
from .Dataset import *

class IrisClassificationTask(Task):
    

    def execute(self, model, modelParameters, session):
        dataset_repo = DatasetRepository(session)
        load_dataset = dataset_repo.get(1) # iris dataset
        load_dataset.data_to_df()
        df = load_dataset.df
        model.fit(load_dataset)
        return model.predict(load_dataset)