import os  # For interacting with the operating system, like file/directory operations
import sys  # Used for getting exception traceback info in CustomException

import numpy as np  # Numerical computing library for handling arrays
import dill  # A better version of pickle used for serializing Python objects
import yaml  # Used to read and write YAML configuration files
from pandas import DataFrame  # Import DataFrame type from pandas

from src.fraudClassifier.exception import CustomException  # Custom error handler for detailed traceability
from src.fraudClassifier import logger  # Project-specific logger for logging messages



def read_yaml_file(file_path: str) -> dict:
    # Reads a YAML file and returns the content as a dictionary
    try:
        with open(file_path, "rb") as yaml_file:  # Open file in binary mode
            return yaml.safe_load(yaml_file)  # Parse YAML content
    except Exception as e:
        raise CustomException(e, sys) from e  # Raise custom error on failure

    


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    # Writes Python object to a YAML file, optionally replacing existing file
    try:
        if replace and os.path.exists(file_path):  # If replace is True and file exists
            os.remove(file_path)  # Remove existing file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create parent directories
        with open(file_path, "w") as file:
            yaml.dump(content, file)  # Dump content to file
    except Exception as e:
        raise CustomException(e, sys) from e  # Handle errors using custom exception

    


def load_object(file_path: str) -> object:
    # Loads a serialized Python object from file using dill
    logger.info("Entered the load_object method of utils")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)  # Deserialize the object
        logger.info("Exited the load_object method of utils")
        return obj
    except Exception as e:
        raise CustomException(e, sys) from e  # Raise error with traceback

    

def save_numpy_array_data(file_path: str, array: np.array):
    # Saves a NumPy array to a binary file using .npy format
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)  # Ensure directory exists
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)  # Save the array
    except Exception as e:
        raise CustomException(e, sys) from e




def load_numpy_array_data(file_path: str) -> np.array:
    # Loads a NumPy array from a .npy file
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)  # Load and return the array
    except Exception as e:
        raise CustomException(e, sys) from e



def save_object(file_path: str, obj: object) -> None:
    # Serializes and saves a Python object using dill
    logger.info("Entered the save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)  # Save the object to file
        logger.info("Exited the save_object method of utils")
    except Exception as e:
        raise CustomException(e, sys) from e



def drop_columns(df: DataFrame, cols: list) -> DataFrame:
    # Drops specified columns from a DataFrame
    logger.info("Entered drop_columns methon of utils")
    try:
        df = df.drop(columns=cols, axis=1)  # Drop the columns
        logger.info("Exited the drop_columns method of utils")
        return df
    except Exception as e:
        raise CustomException(e, sys) from e
