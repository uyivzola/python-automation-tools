import os
import datetime as dt
import shutil


def get_file_info(file_path):
    """
    Retrieve information about a file.
    """
    file_stats = os.stat(file_path)
    file_size = file_stats.st_size
    modified_time = dt.datetime.fromtimestamp(file_stats.st_mtime)
    created_time = dt.datetime.fromtimestamp(file_stats.st_ctime)
    return file_size, modified_time, created_time


def traverse_directory(root_dir):
    """
    Traverse a directory tree and perform actions on files.   
    """
    for root, directories, files in os.walk(root_dir):
        print("Current directory: " + root)

        for directory in directories:
            print('Subdirectory of ' + root + ":" + directory)

            for file in files:
                file_path = os.path.join(root, file)
                file_size, modified_time, created_time = get_file_info(
                    file_path)

                print('File in '+root+":" + file)
                print('File size '+str(file_size)+'bytes')
                print('Modified time' + str(modified_time))
                print('Created time '+str(created_time))
                print('File path ' + os.path.abspath(file_path))

                # RENAME THE FILE WITH A TIMESTAMP
                timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
                new_file_name = timestamp + "_" + file
                new_file_path = os.path.join(root, new_file_name)
                os.rename(file_path, new_file_path)
                print("Renamed file: " + new_file_name)

                # MOVE FILES TO SUBDIRS BASED ON FILE EXTENSION
                file_extension = os.path.splitext(file)[1][1:].lower()
                destination_folder = os.path.join(root, file_extension)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(new_file_path, os.path.join(
                    destination_folder, new_file_name))
                print('Move file to ' + destination_folder)
