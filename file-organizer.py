import os
import datetime as dt

def get_file_info(file_path):
    """
    Retrieve information about a file.
    """
    file_stats = os.stat(file_path)
    file_size = file_stats.st_size
    modified_time = datetime.datetime.fromtimestamp(file_stats.st_mtime)
    created_time = datetime.datetime.fromtimestamp(file_stats.st_ctime)
    return file_size, modified_time, created_time
