
class EvaluationProcedure():
   
    def __init__(self):
        self.name = type(self).__name__
        self.object = None 

    def evaluate(self, **kwargs):
        raise NotImplementedError('Classe abstrata')

  
