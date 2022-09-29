from pathlib import Path
from shutil import copytree
import argparse

from .docs import build_docs
from .web import build_site
from .paths import pages_dir
from .config import config


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", type=str, help="The CycloneDDS Pro version tag.", required=True)
    parser.add_argument("--project-c", type=str, help="Path to C project")
    parser.add_argument("--project-cpp", type=str, help="Path to C++ project")
    parser.add_argument("--project-py", type=str, help="Path to Python project")
    return parser.parse_args()


def main():
    namespace = parse()

    build_docs("cyclonedds", config["projects"]["cyclonedds"], Path(namespace.project_c).resolve(), namespace.version, pages_dir)
    build_docs("cyclonedds-cxx", config["projects"]["cyclonedds-cxx"], Path(namespace.project_cpp).resolve(), namespace.version, pages_dir)
    build_docs("cyclonedds-python", config["projects"]["cyclonedds-python"], Path(namespace.project_py).resolve(), namespace.version, pages_dir)

    build_site(namespace.version, config, pages_dir)


if __name__ == "__main__":
    main()
