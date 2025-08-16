class Task():


    def __init__(self):
        raise NotImplementedError('Classe abstrata')
    
    def set_dataset(self,dataset):
        self.dataset = dataset

    def set_model(self,model):
        self.model = model

    def execute(self,  parameters):
        raise NotImplementedError('Classe abstrata')
    
    def set_target_feature_name(self, target_feature_name):
        self.target_feature_name = target_feature_name

