import os
import sys

# working_directory = ""

def get_files_info(working_directory, directory=None):
    print(os.path.abspath(directory), os.path.abspath(working_directory))
    if not os.path.abspath(os.path.join(working_directory, directory)).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif (not os.path.isdir(os.path.join(working_directory, directory))):
        return f'Error: "{directory}" is not a directory' 

    dir_info = []
    path = os.path.join(working_directory, directory)
    for item in os.listdir(os.path.join(working_directory, directory)):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            try:
                dir_info.append(f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir=False")
            except Exception:
                return "Error: Getting path size failed"
        if os.path.isdir(item_path):
            try:
                dir_info.append(f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir=True")
            except Exception:
                return "Error: funciton failed"
    return "\n".join(dir_info)


