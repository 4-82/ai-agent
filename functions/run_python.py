import os
import sys
import subprocess

def run_python_file(working_directory, file_path):
    directory_path = os.path.abspath(working_directory)
    file_info = os.path.join(working_directory, file_path)

    print(f"Checking paths, working_directory: {directory_path}, filepath: {file_info}")

    if not os.path.abspath(file_info).startswith(directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(file_info):
        return f'Error: File "{file_path}" not found'
    elif not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            [sys.executable, file_info],
            capture_output=True,
            text=True,
            cwd=".",
            timeout=30
        )    
    except Exception as e:
        return f"Error: executing Python file: {e}"

    stdout = f'STDOUT: \n{result.stdout}\n'
    stderr = f'STDERR: \n{result.stderr}\n'
    process_info = f'Process exited with code {result.returncode}\n'  
    output = f'{stdout} {stderr}'
    
    if result.returncode != 0:
        output += process_info
    if result.stdout == "" and result.stderr == "":
        output += 'No output produced'

    return output

print(run_python_file("calculator", "main.py"))
 
