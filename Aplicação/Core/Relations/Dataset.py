class Dataset():

    def __init__(self, **kwargs):
        self.targetFeature = kwargs.get("targetFeature", None) 
        self.df = kwargs.get("df", None) 

