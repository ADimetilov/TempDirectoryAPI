import datetime
import os
from time import time
import schedule
from .Worker_config import WConfig
from .config import NAME_FILE_CONFIG, TIME_DELETE_DIRECTORY, DIR
from .Worker_directory import WDirectory

class WShendule:
    def __init__(self): # Initialize the scheduler and set up the job to delete directories at the specified time
        #If the time for deleting directories is not set, the scheduler will not be started
        self._func()
        schedule.every().day.at(TIME_DELETE_DIRECTORY).do(self._func)
        schedule.run_pending()

    def _func(self): # Function for deleting directories if time for exists
        directories = WDirectory.get_directories()
        for directory in directories:
            file_path = os.path.join(DIR,directory, NAME_FILE_CONFIG)
            print(file_path)
            config_data = WConfig.load_config_file(file_path)
            print(config_data)
            if config_data.get("date_delete") == datetime.datetime.now().strftime("%Y-%m-%d"):
                WDirectory.remove(directory.split("_", 1)[0])