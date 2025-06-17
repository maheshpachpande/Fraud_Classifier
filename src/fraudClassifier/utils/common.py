import os  # For interacting with the OS (creating/removing files/folders)
import sys  # For capturing detailed exception info using sys.exc_info()
import numpy as np  # Used for numerical operations and array handling
import dill  # Used for serializing Python objects (like pickle, but more robust)
import yaml  # To read/write YAML configuration files
from pandas import DataFrame  # Import DataFrame class from pandas for tabular data

from ensure import ensure_annotations  # To enforce type annotations at runtime
from src.fraudClassifier.exception import CustomException  # Custom exception class with file/line info
from src.fraudClassifier import logger  # Custom logger for logging pipeline stages/messages


@ensure_annotations  # Ensures function arguments and return types follow annotations
def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its content as a dictionary.
    """
    try:
        with open(file_path, "rb") as yaml_file:  # Open YAML file in binary mode
            return yaml.safe_load(yaml_file)  # Load and return YAML content as Python dict
    except Exception as e:
        raise CustomException(e, sys) from e  # Raise custom error with traceback details


@ensure_annotations
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes Python object to YAML file. Replaces existing file if specified.
    """
    try:
        if replace and os.path.exists(file_path):  # If replace is True and file already exists
            os.remove(file_path)  # Delete the existing file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories if needed
        with open(file_path, "w") as file:  # Open file in write mode
            yaml.dump(content, file)  # Dump the object into YAML file
    except Exception as e:
        raise CustomException(e, sys) from e  # Raise custom error with context


@ensure_annotations
def load_object(file_path: str) -> object:
    """
    Loads a serialized Python object from file using dill.
    """
    logger.info("Entered the load_object method of utils")  # Log function entry
    try:
        with open(file_path, "rb") as file_obj:  # Open file in binary read mode
            obj = dill.load(file_obj)  # Load object using dill
        logger.info("Exited the load_object method of utils")  # Log function exit
        return obj  # Return the deserialized object
    except Exception as e:
        raise CustomException(e, sys) from e

@ensure_annotations
def save_object(file_path: str, obj: object) -> None:
    """
    Serializes and saves a Python object using dill.
    """
    logger.info("Entered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
        with open(file_path, "wb") as file_obj:  # Open file in binary write mode
            dill.dump(obj, file_obj)  # Serialize object to file
        logger.info("Exited the save_object method of utils")
    except Exception as e:
        raise CustomException(e, sys) from e


@ensure_annotations
def save_numpy_array_data(file_path: str, array: np.ndarray) -> None:
    """
    Saves NumPy array to a .npy binary file.
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create dir if missing
        with open(file_path, "wb") as file_obj:  # Open file for binary write
            np.save(file_obj, array)  # Save NumPy array to file
    except Exception as e:
        raise CustomException(e, sys) from e

@ensure_annotations
def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    Loads NumPy array from a .npy file.
    """
    try:
        with open(file_path, "rb") as file_obj:  # Open file for binary read
            return np.load(file_obj)  # Load and return NumPy array
    except Exception as e:
        raise CustomException(e, sys) from e


@ensure_annotations
def drop_columns(df: DataFrame, cols: list[str]) -> DataFrame:
    """
    Drops specified columns from a DataFrame and returns the result.
    """
    logger.info("Entered drop_columns method of utils")  # Log method entry
    try:
        df = df.drop(columns=cols, axis=1)  # Drop columns from DataFrame
        logger.info("Exited the drop_columns method of utils")  # Log method exit
        return df  # Return updated DataFrame
    except Exception as e:
        raise CustomException(e, sys) from e

