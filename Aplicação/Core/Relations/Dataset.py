import pandas as pd

class Dataset():

    def __init__(self, **kwargs):
        self.targetFeature = kwargs.get("targetFeature", None)  
        self.name = kwargs.get("name", None) 
        self.features = kwargs.get("features", None)  


    def generate_df(self):
        df = pd.DataFrame(self.features, columns = ['feature_obj'])
        df['name'] = df['feature_obj'].map(lambda x: x.name)
        df['value'] = df['feature_obj'].map(lambda x: x.value)
        df['type'] = df['feature_obj'].map(lambda x: x.type)
        df['timestamp'] = df['feature_obj'].map(lambda x: x.timestamp)
        df.drop(columns = ['feature_obj'], inplace= True)
        df['value'] = df.apply(lambda x : eval(x['type'])(x['value'])  ,axis = 1)
        df_data = df.pivot_table(index = ['timestamp'], values= ['value'], columns= 'name', aggfunc='max')
        df_data.columns = [i[1] for i in df_data.columns]
        df_data = df_data.reset_index()
        self.df=  pd.DataFrame(df_data.to_dict())
            
  