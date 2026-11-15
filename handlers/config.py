import os

DIR = os.path.join(os.getcwd(),"Data") # Get the current working directory
TIME_STORAGE = 30 # Time to store directories (in days)
TIME_DELETE_DIRECTORY = "00:00" # Time to delete directories (in 24-hour format)
NAME_FILE_CONFIG =  "config_directory.json" # Name of the configuration file for directories
NAME_TEMPLATE = "(\d+)_(\w+)" # Template for naming files in the directories