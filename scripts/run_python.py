import subprocess

def run_python_file(file_path):
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred while running the file: {e.stderr}"

