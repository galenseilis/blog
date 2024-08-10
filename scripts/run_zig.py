import subprocess
import os
import stat

def log_permissions(path):
    st = os.stat(path)
    permissions = stat.filemode(st.st_mode)
    print(f"Permissions for {path}: {permissions}")

def find_executable(bin_dir):
    """Find the executable file in the given directory."""
    for root, dirs, files in os.walk(bin_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.access(file_path, os.X_OK):
                return file_path
    raise FileNotFoundError("No executable found in the bin directory.")

def build_and_run_zig(project_dir):
    project_dir = os.path.abspath(project_dir)

    # Build the Zig project
    try:
        build_process = subprocess.run(
            ['zig', 'build'],
            cwd=project_dir,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Build Error: {e.stderr}")
        return

    # Find the executable in the zig-out/bin/ directory
    bin_dir = os.path.join(project_dir, 'zig-out', 'bin')
    if not os.path.exists(bin_dir):
        raise FileNotFoundError("The bin directory does not exist after the build.")
    
    exe_path = find_executable(bin_dir)

    # Set the executable permissions
    try:
        os.chmod(exe_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
    except PermissionError as e:
        print(f"Error setting permissions: {e}")
        return

    # Run the compiled executable and print its output
    try:
        run_process = subprocess.run(
            [exe_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # print(run_process.stdout)  # Print the output from the Zig executable
        # print(run_process.stderr)  # Print any error output
        if run_process.stdout:
            return run_process.stdout
        else:
            return run_process.stderr
    except subprocess.CalledProcessError as e:
        print(f"Execution Error: {e.stderr}")
        return

# Example usage
if __name__ == "__main__":
    output = build_and_run_zig('/home/galen/projects/blog/posts/zig-run-from-python/hello')

