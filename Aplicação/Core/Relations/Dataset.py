import io
import pandas as pd

class Dataset():

    def __init__(self, **kwargs):
        self.targetFeature = kwargs.get("targetFeature", None)  
        self.name = kwargs.get("name", None) 
        self.data = kwargs.get("data", None) 
        self.df = kwargs.get("df", None) 
        if self.data is not None and self.df is None:
            self.data_to_df()
        elif self.data is None and self.df is not None:
            self.df_to_data()

    def df_to_data(self):
        if self.df is not None:
            buffer = io.BytesIO()
            self.df.to_parquet(buffer, engine='pyarrow')
            self.data = buffer.getvalue()

    def data_to_df(self):
        if self.data is not None:
            buffer = io.BytesIO(self.data)
            self.df = pd.read_parquet(buffer, engine='pyarrow')

    