
from .BaseStorageHandler import BaseStorageHandler
from pathlib import Path
import os
import sys
from io import BytesIO

class LocalStorageHandler(BaseStorageHandler):

    def __init__(self, root= '.\\'):
        self.root = root

        # create path
        Path(root).mkdir(parents=True, exist_ok=True)
        sys.path.append(".")

    def save(self, path, buffer):
        full_path = os.path.join(self.root , path)
        full_path_without_file_array = full_path.split('\\')[:-1]
        full_path_without_file = '\\'.join(full_path_without_file_array)

        Path(full_path_without_file).mkdir(parents=True, exist_ok=True)
        f =  open(full_path, "wb") 
        f.write(buffer.getbuffer())
        f.close()
        
    def load(self, path):
        full_path = os.path.join(self.root , path)
        f = open(full_path, "rb")
        buffer = BytesIO(f.read())
        f.close()
        return buffer

    def list_files(self, path):
        full_path = os.path.join(self.root , path)
        return os.listdir(full_path)
        
