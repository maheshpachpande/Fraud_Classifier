import sys  # Import the sys module to access exception details using sys.exc_info()
from types import TracebackType  # Used for typing the traceback object
from typing import Optional  # Allows a variable to be of a specified type or None


# Function to format a detailed exception message with filename and line number
def format_exception_message(error: Exception, error_detail: Optional[TracebackType] = None) -> str:
    """
    Formats a detailed error message with file name and line number.
    """
    exc_type, exc_obj, tb = sys.exc_info()  # Extract the current exception's traceback details
    if tb is None:
        return str(error)  # If traceback is not available, return the error message only

    file_name = tb.tb_frame.f_code.co_filename  # Get the filename where the exception occurred
    line_number = tb.tb_lineno  # Get the exact line number of the error
    return f"[{file_name}] Line {line_number}: {str(error)}"  # Return a formatted string with file and line


# Custom exception class that extends Python's built-in Exception class
class CustomException(Exception):
    """
    Custom Exception class that includes file name and line number in error messages.
    """
    def __init__(self, error: Exception):
        super().__init__(str(error))  # Initialize the base Exception class with the error message
        self.message = format_exception_message(error)  # Generate the detailed error message

    def __str__(self) -> str:
        return self.message  # When str() is called on this exception, return the detailed message
