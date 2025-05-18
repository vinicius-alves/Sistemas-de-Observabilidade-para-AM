class Prediction():
 
     def __init__(self, **kwargs):
         self.value = kwargs.get("value", None)  
         self.type = kwargs.get("type", None)
         self.run = kwargs.get("run", None) 
         self.timestamp = kwargs.get("timestamp", None) 
         self.idEntity = kwargs.get("idEntity", None) 