import os
import sys
from pathlib import Path
from shutil import rmtree, copyfile
import subprocess

from .paths import pages_dir
from .build_prep import build_wrap


def build_docs(project: str, config: dict, repo_path: Path, version: str, out_path: Path):
    _run_build(project, config['name'], repo_path, out_path / "docs" / project, config, version)


def _run_build(project: str, project_name: str, repo_path: Path, out_path: Path, config: dict, version: str):
    confpy = list((repo_path / "docs").rglob("**/conf.py"))
    if not confpy:
        print(f"No conf.py, not building {project_name}")
        return False
    print(f"Building {project_name}")

    try:
        rmtree(out_path)
    except:
        pass

    out_path.mkdir(parents=True, exist_ok=True)
    with build_wrap(project, repo_path, confpy[0], version):
        env = os.environ.copy()
        env["PYTHONPATH"] = os.sep.join(sys.path)

        p = subprocess.Popen([
            sys.executable,
            "-m",
            "sphinx",
            str(confpy[0].parent),
            str(out_path)
        ], env=env, cwd=repo_path)
        p.communicate()

    if not (out_path / "index.html").exists():
        rmtree(out_path)
        return False

    copyfile(str(pages_dir / "js" / "docu.js"), str(out_path / "_static" / "docu.js"))
    copyfile(str(pages_dir / "css" / "docu.css"), str(out_path / "_static" / "docu.css"))

    return True

