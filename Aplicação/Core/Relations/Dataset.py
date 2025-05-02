import pandas as pd

class Dataset():

    def __init__(self, **kwargs): 
        self.name = kwargs.get("name", None)  
        self.df = kwargs.get("df", None)  
  