import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=None):
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
        commands = [sys.executable, file_info]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=".",
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}" 
