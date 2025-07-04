class SubjectEntity():

    def __init__(self,  **kwargs):
        self.idEntity = kwargs.get("idEntity", None)  
        self.timestamp = kwargs.get("timestamp", None) 