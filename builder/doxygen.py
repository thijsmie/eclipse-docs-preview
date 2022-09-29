import subprocess
import re
from pathlib import Path


def run_doxygen(path: Path, config_file: Path):
    p = subprocess.Popen([
        "doxygen",
        str(config_file),
    ], cwd=path, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.communicate()

