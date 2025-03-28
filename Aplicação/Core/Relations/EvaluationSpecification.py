from .Task import Task 
from .EvaluationProcedure import EvaluationProcedure

class EvaluationSpecification():

    def __init__(self, tasks : Task, evaluationProcedures: EvaluationProcedure):
        self.tasks = tasks
        self.evaluationProcedures = evaluationProcedures
  