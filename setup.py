#!/usr/bin/python3
"""Setup module for code_interview pkg."""
from setuptools import setup, find_packages
import os
import sys
import shutil
import stat
from setuptools.command.develop import develop
from setuptools.command.install import install
from abstract_requires import requires

pkg_name = "code_interview"
parent_dir = os.path.dirname(os.path.realpath(__file__))
data_src_dir = pkg_name + "_data"
config_src_dir = pkg_name + "_config"
defaults_location = os.path.join(pkg_name, "defaults")

# Create scripts list
script_dir = os.path.join(parent_dir, "bin")
scripts = []
try:
    for f in os.listdir(script_dir):
        scripts.append(os.path.join(script_dir, str(f)))

except FileNotFoundError:
    pass


def reset():
    """Remove build dirs."""
    dirnames_to_remove = [pkg_name + ".egg-info", "dist", "build"]
    for d in dirnames_to_remove:
        shutil.rmtree(d, ignore_errors=True)


def setuptools_setup():
    """Setup provisioner."""
    setup(
        name="code_interview",
        version="0.1",
        description="Solutions to questions from \"Cracking the Coding Interview\" by Gayle McDowell.",
        url="https://github.com/ku-wolf/code_interview",
        author="Kevin Wolf",
        author_email="kevinuwolf@gmail.com",
        license="gplv3.txt",
        packages=find_packages(),
        scripts=scripts,
        install_requires=requires,
        setup_requires=requires,
    )


def main():
    """Main method."""
    os.chdir(parent_dir)

    if sys.argv[1] == "reset":
        reset()
    else:
        setuptools_setup()

if __name__ == "__main__":
    main()
