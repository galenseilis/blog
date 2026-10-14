"""Find #nosec comments in the installed bandit package."""
from pathlib import Path
import subprocess

import bandit

if __name__ == "__main__":
    init_path = Path(bandit.__file__).parent
    print(subprocess.run(['grep', '-rin', r'\#\snosec', init_path], capture_output=True, text=True).stdout)
