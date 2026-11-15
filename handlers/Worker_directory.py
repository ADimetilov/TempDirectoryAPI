from datetime import datetime, timedelta
import json
import os
from .config import DIR, NAME_TEMPLATE, TIME_STORAGE, NAME_FILE_CONFIG
import re
import shutil

class WDirectory:

    @staticmethod
    def get_file_for_directory(directory_id: int): # Get a list of all files in the specified directory
        directories = WDirectory.get_directories()
        directory_name = None
        for directory in directories:
            if re.match(NAME_TEMPLATE, directory):
                id = int(re.search(r'(\d+)', directory).group())
                if id == int(directory_id):
                    directory_name = directory
                    break
        if not directory_name:
            return []
        directory_path = os.path.join(DIR, directory_name)
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    @staticmethod
    def get_directory_path(directory_id: int): # Get the path of the specified directory
        directories = WDirectory.get_directories()
        for directory in directories:
            if re.match(NAME_TEMPLATE, directory):
                id = int(re.search(r'(\d+)', directory).group())
                if id == int(directory_id):
                    directory_name = directory
                    break
        return os.path.join(DIR, directory_name)

    @staticmethod
    def get_directories(): # Get a list of all directories in the specified directory
        return [d for d in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, d))]

    @staticmethod
    def remove(directory_id: int): # Remove the specified directory from the specified directory
        directories = WDirectory.get_directories()
        for directory in directories:
            if re.match(NAME_TEMPLATE, directory):
                id = int(re.search(r'(\d+)', directory).group())
                if id == int(directory_id):
                    directory_name = directory
                    break
        directory_path = os.path.join(DIR, directory_name)
        shutil.rmtree(directory_path)

    @staticmethod
    def create(directory_name: str, day: int | None = None): # Create a new directory with the specified name in the specified directory
        directories = WDirectory.get_directories()
        if len(directories) > 0:
            print(directories[-1])
            id = int(re.search(r'(\d+)', directories[-1]).group())
            id +=1
        else:
            id = 1
        directory_name = str(id)+"_" + directory_name
        directory_path = os.path.join(DIR, directory_name)
        os.makedirs(directory_path, exist_ok=True)
        data = {
            "date_create": datetime.now().strftime("%Y-%m-%d"),
            "date_delete": (datetime.now() + timedelta(days=TIME_STORAGE)).strftime("%Y-%m-%d") if day is None 
                else (datetime.now() + timedelta(days=day)).strftime("%Y-%m-%d")
            }
        json.dump(data, open(os.path.join(DIR, directory_name, NAME_FILE_CONFIG), 'w'))