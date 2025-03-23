
class EvaluationProcedure():
   
    def __init__(self, name):
        self.name = name

    def evaluate(self, **kwargs):
        raise NotImplementedError('Classe abstrata')

  
