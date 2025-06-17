import os # for file and directory operations
from pathlib import Path # for handling file paths
# for logging messages
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "fraudClassifier"

list_of_files = [
    ".github/workflows/.gitkeep", # to Git track the directory
    f"src/{project_name}/__init__.py", # to make src a package
    f"src/{project_name}/components/__init__.py",# for data ingestion, validation, transformation etc.
    f"src/{project_name}/utils/__init__.py",# to make utils a package
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", # stores centralized configuration files
    f"src/{project_name}/pipeline/__init__.py", # step-by-step execution flow of the machine learning
    f"src/{project_name}/entity/__init__.py", # used to define structured data models (often with dataclasses) that represent core components passed between pipeline stages.
    f"src/{project_name}/constants/__init__.py", # used to store fixed values (like config keys or thresholds) in one place to ensure consistency and easy maintenance across the codebase.
    "config/config.yaml", # main configuration file for the project
    "dvc.yaml", # DVC pipeline file that defines the stages of the machine learning workflow
    "params.yaml", # parameters for the DVC pipeline, such as model hyperparameters or data processing settings
    "requirements.txt", # Python package dependencies for the project
    "setup.py", # script for installing the project as a package
    "research/trials.ipynb",
    "templates/index.html"


]


# Create directories and files if they do not exist
# Iterate through the list of files and create directories and files as needed
for filepath in list_of_files:
    filepath = Path(filepath) # Convert to Path object for better path handling
    filedir, filename = os.path.split(filepath) # Split the path into directory and filename


    if filedir !="": # Check if the directory part is not empty
        os.makedirs(filedir, exist_ok=True) # Create the directory if it does not exist
        logging.info(f"Creating directory; {filedir} for the file: {filename}") # Log the creation of the directory
    # Check if the file already exists or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f: # Open the file in write mode
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")