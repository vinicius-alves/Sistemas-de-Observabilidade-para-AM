class Feature():

    def __init__(self,  idFeature = None, name = None, nameSpace = None):
        self.idFeature = idFeature 
        self.name = name
        self.nameSpace = nameSpace

    def get_full_name(self):
        return str(self.nameSpace.name) +'__'+self.name

 