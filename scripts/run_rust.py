import subprocess
import os
import stat

def log_permissions(path):
    st = os.stat(path)
    permissions = stat.filemode(st.st_mode)
    print(f"Permissions for {path}: {permissions}")

def compile_and_run_rust(target_file):
    # Get the directory and the file name
    target_dir = os.path.dirname(target_file)
    target_name = os.path.basename(target_dir)  # Adjusted to get the correct target name

    # Ensure Cargo.toml exists in the target directory
    cargo_toml_path = os.path.join(target_dir, 'Cargo.toml')
    if not os.path.exists(cargo_toml_path):
        raise FileNotFoundError("Cargo.toml not found in the target directory.")

    # Compile the Rust project
    try:
        build_process = subprocess.run(
            ['cargo', 'build', '--release'],
            cwd=target_dir,
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Compilation Error: {e.stderr}")
        return

    # Find the compiled executable
    target_exe = os.path.join(target_dir, 'target', 'release', target_name)
    if os.name == 'nt':
        target_exe += '.exe'

    if not os.path.exists(target_exe):
        raise FileNotFoundError("Compiled executable not found.")

    if os.name != 'nt':
        try:
            os.chmod(target_exe, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
            os.chmod(os.path.dirname(target_exe), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
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
    output = compile_and_run_rust('../posts/rust-run-from-python/hello/main.rs')
    print(output)

