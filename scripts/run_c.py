import subprocess
import os
import glob
import stat

def log_permissions(path):
    st = os.stat(path)
    permissions = stat.filemode(st.st_mode)
    print(f"Permissions for {path}: {permissions}")

def compile_and_run_c(project_dir):
    project_dir = os.path.abspath(project_dir)
    
    # Find all .c files in the project directory
    c_files = glob.glob(os.path.join(project_dir, '*.c'))
    if not c_files:
        raise FileNotFoundError("No C source files found in the project directory.")

    object_files = []

    # Compile each .c file into an object file
    for c_file in c_files:
        obj_file = os.path.splitext(c_file)[0] + '.o'
        try:
            compile_process = subprocess.run(
                ['gcc', '-c', c_file, '-o', obj_file],
                cwd=project_dir,
                check=True,
                capture_output=True,
                text=True
            )
            object_files.append(obj_file)
        except subprocess.CalledProcessError as e:
            print(f"Compilation Error for {c_file}: {e.stderr}")
            return

    # Determine the name of the executable (assuming the file with main is called main.c)
    exe_name = 'program'
    main_file = os.path.join(project_dir, 'main.c')
    if os.path.exists(main_file):
        exe_name = os.path.splitext(os.path.basename(main_file))[0]
    
    # Link all object files into a single executable
    try:
        link_process = subprocess.run(
            ['gcc', '-o', exe_name] + object_files,
            cwd=project_dir,
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Linking Error: {e.stderr}")
        return

    # Find the compiled executable
    target_exe = os.path.join(project_dir, exe_name)

    if not os.path.exists(target_exe):
        raise FileNotFoundError("Compiled executable not found.")

    # Set the executable permissions
    try:
        os.chmod(target_exe, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
    except PermissionError as e:
        print(f"Error setting permissions: {e}")
        return

    # Run the compiled executable and capture its output
    try:
        run_process = subprocess.run(
            [target_exe],
            check=True,
            capture_output=True,
            text=True
        )
        output = run_process.stdout
        return output
    except subprocess.CalledProcessError as e:
        print(f"Execution Error: {e.stderr}")
        return

# Example usage
if __name__ == "__main__":
    output = compile_and_run_c('../posts/c-run-from-python/hello')
    print(output)

