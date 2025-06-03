
class EvaluationProcedure():
   
    def __init__(self, name = None):
        if name is None:
            self.name = type(self).__name__

    def evaluate(self, **kwargs):
        raise NotImplementedError('Classe abstrata')

  
