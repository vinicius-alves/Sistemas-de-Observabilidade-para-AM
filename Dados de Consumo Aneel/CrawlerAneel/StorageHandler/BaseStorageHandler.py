
class BaseStorageHandler:

    def save(self, path, buffer):
        raise NotImplementedError('método abstrato')
        
    def load(self, path):
        raise NotImplementedError('método abstrato')

    def list_files(self, path):
        raise NotImplementedError('método abstrato')

    def list_directories(self, path):
        raise NotImplementedError('método abstrato')
        
