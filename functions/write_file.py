import os
import sys

def write_file(working_directory, file_path, content):
    directory_path = os.path.abspath(working_directory)
    file_info = os.path.join(working_directory, file_path)

    print(f"Checking paths, working_directory: {directory_path}, filepath: {file_info}")

    if not os.path.abspath(file_info).startswith(directory_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(file_info):
        try:
            os.makedirs(os.path.join(working_directory, os.path.dirname(file_path)), exist_ok=True)       
        except Exception as e:
            return f"Error: {e}"

    with open(file_info, "w") as file:
        file.write(content)
    file.close()

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
