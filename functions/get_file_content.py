import os

def get_file_content(working_directory, file_path):

    directory_path = os.path.abspath(working_directory)
    file_info = os.path.join(working_directory, file_path)

    print(f"Checking paths, working_directory: {directory_path}, filepath: {file_info}")

    if not os.path.abspath(file_info).startswith(directory_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(file_info):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(file_info, "r") as file:
            file_text = file.read()
        file.close()
    except Exception:
        return f'Something went wrong when interacting with the file at {file_info}'

    if len(file_text) > 10000:
        return "".join(file_text[:10000]) + f'\n\n[...File "{file_path}" truncated at 10000 characters]'
    return file_text
    
