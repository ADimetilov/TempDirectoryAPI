import os
import sys
import json
class WConfig:

    @staticmethod
    def create_config_file(file_path, config_data): # Create a configuration file with the specified data
        with open(file_path, 'w') as file:
            file.write(config_data)

    @staticmethod
    def load_config_file(file_path): # Load the configuration data from the specified file
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r') as file:
            return json.load(file)
