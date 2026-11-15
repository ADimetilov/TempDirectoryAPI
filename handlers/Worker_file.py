from .Worker_directory import WDirectory
import os
import re
from .config import NAME_TEMPLATE, DIR
class WFile:

    @staticmethod
    def get_last_id_directories(id:int): # Get the ID of the specified file
        files = WDirectory.get_file_for_directory(id)
        print(files)
        if len(files) > 1 and re.match(r'(\d+)_', files[-2]):
            id = int(re.search(r'(\d+)', files[-2]).group())
            return id + 1
        else:
            return 1

    @staticmethod
    def get_file_name(id_directory:int, file_id:int): # Get the name of the specified file
        files = WDirectory.get_file_for_directory(id_directory)
        for file in files:
            if re.match(NAME_TEMPLATE, file):
                id = int(re.search(r'(\d+)', file).group())
                if id == int(file_id):
                    return file.split("_", 1)[1]

    @staticmethod
    def get_file_path(directory_id: int, file_id: int) -> str: # Get the path of the specified directory
        files = WDirectory.get_file_for_directory(directory_id)
        DIR = WDirectory.get_directory_path(directory_id)
        for file in files:
                    if re.match(NAME_TEMPLATE, file):
                        id = int(re.search(r'(\d+)', file).group())
                        if id == int(file_id):
                            file_name = file
                            break
        return os.path.join(DIR, file_name)

        
    @staticmethod
    def read_file(id:int,file_id:int): # Read the contents of the specified file and return it as a string
        files = WDirectory.get_file_for_directory(id)
        if files:
            file_path = WFile.get_file_path(id, file_id)
            with open(file_path, 'r') as file:
                return file.read()
        return ""

    @staticmethod
    def write_file(id_directory:int, filename: str, content: bytes) -> True:
        filename = str(WFile.get_last_id_directories(id_directory)) + "_" + filename
        file_path = os.path.join(WDirectory.get_directory_path(id_directory), filename)
        # Write the specified content to the specified file, overwriting any existing content
        with open(file_path, 'wb') as file:
            file.write(content)

    @staticmethod
    def delete_file(id_directory:int, file_id: int) -> True:
        filename = WFile.get_file_name(id_directory, file_id)
        file_path = os.path.join(WDirectory.get_directory_path(id_directory), filename)
        # Delete the specified file
        os.remove(file_path)