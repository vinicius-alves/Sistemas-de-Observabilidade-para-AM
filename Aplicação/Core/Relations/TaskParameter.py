
class TaskParameter():

    def __init__(self, name = None, value = None, type = None):
        self.name = name
        self.value = value
        self.type = type

    def process_type(self):
        self.type = self.value.__class__.__name__
        self.value = str(self.value)
