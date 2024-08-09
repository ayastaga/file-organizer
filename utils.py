# utils.py

import os
import shutil
import time
from distutils.dir_util import copy_tree
from config import SLEEP_TIME, FILE_TYPE_LIST

def display_files(path, text_widget):
    text_widget.delete('1.0', tk.END)
    for root, dirs, files in os.walk(path):
        for file in files:
            text_widget.insert(tk.END, f"{os.path.join(root, file)}\n")
            text_widget.update()
            time.sleep(SLEEP_TIME)

def organize_by_extension(path):
    for file_ in os.listdir(path):
        name, ext = os.path.splitext(file_)
        ext = ext[1:]

        if ext == '':
            continue

        destination_folder = os.path.join(path, ext)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        shutil.move(os.path.join(path, file_), os.path.join(destination_folder, file_))

def organize_by_type(path, file_type_list):
    for file_ in os.listdir(path):
        ext = ''
        if '.' in file_:
            ext = file_.split('.')[1]

        folder_ext = 'Others'
        for file_type in file_type_list:
            if ext in file_type_list[file_type]:
                folder_ext = file_type

        destination_folder = os.path.join(path, folder_ext)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        shutil.move(os.path.join(path, file_), os.path.join(destination_folder, file_))

def organize_by_custom(path, log_dict):
    for file_ in os.listdir(path):
        name, ext = os.path.splitext(file_)
        ext = ext[1:]

        for i in range(1, 6):
            try:
                if ext not in log_dict[i][1]:
                    continue
                
                if not any(keyword in name for keyword in log_dict[i][2]):
                    continue
                
                destination_folder = os.path.join(path, log_dict[i][0])
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                shutil.move(os.path.join(path, file_), os.path.join(destination_folder, file_))
                break
            except IndexError:
                pass  # Skip if the log_dict entry is empty

def delete_files(file_path):
    try:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))
    except OSError as e:
        print(f"Error occurred while deleting files: {e}")

def copy_folder(original_path):
    return shutil.copytree(original_path, f"{original_path}_copy")

def copy_folder_contents(src, dst):
    copy_tree(src, dst)