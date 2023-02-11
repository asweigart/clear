import io
import os
import re
from setuptools import setup, find_packages

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

# Find version info from module (without importing the module):
with open("src/clear/__init__.py", "r") as fileObj:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fileObj.read(), re.MULTILINE
    ).group(1)

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

setup(
    name="clear",
    version=version,
    url="https://github.com/asweigart/clear",
    author="Al Sweigart",
    author_email="al@inventwithpython.com",
    description=("""A cross-platform Python module that provides a clear() function which clears the terminal. That's all."""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    keywords="",
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",

    ],
)
