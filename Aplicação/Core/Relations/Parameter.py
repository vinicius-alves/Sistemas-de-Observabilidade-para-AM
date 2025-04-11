
class Parameter():

    def __init__(self, name = None, value = None):
        self.name = name
        self.value = value

    def process_type(self):
        self.valueType = self.value.__class__.__name__
        self.value = str(self.value)