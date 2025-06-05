class Feature():

    def __init__(self,  idFeature = None, name = None, nameSpace = None, idFeatureNameSpace = None):
        self.idFeature = idFeature 
        self.name = name
        self.nameSpace = nameSpace
        self.idFeatureNameSpace = idFeatureNameSpace

    def get_full_name(self):
        #return str(self.nameSpace.name) +'__'+self.name
        return self.name

 