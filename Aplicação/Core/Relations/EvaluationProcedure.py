
class EvaluationProcedure():
   
    def __init__(self):
        self.name = type(self).__name__

    def evaluate(self, **kwargs):
        raise NotImplementedError('Classe abstrata')

  
