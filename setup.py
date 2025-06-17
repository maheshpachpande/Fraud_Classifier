from setuptools import setup, find_packages  # Imports setup tools: setup() for packaging config, find_packages() to auto-detect all Python packages

# Calls the setup function to define package metadata and structure
setup(
    name="fraudClassifier",  # Name of the package to be used in PyPI or local installs
    version="0.0.0",  # Initial version of the package
    author="Mahesh",  # Author's name
    author_email="pachpandemahesh300@gmail.com",  # Contact email of the author
    packages=find_packages()  # Automatically finds all Python packages (directories with __init__.py) in the current directory
)
