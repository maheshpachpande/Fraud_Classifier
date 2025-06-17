import os  # Provides functions for interacting with the operating system (like file paths, directories)
import sys  # Allows access to system-specific parameters and functions (used here for stdout)
import logging  # Python’s built-in logging library for tracking events and debugging

# Defines the log message format with timestamp, log level, module name, and message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"  # Directory where log files will be stored
log_filepath = os.path.join(log_dir, "running_logs.log")  # Full path of the log file
os.makedirs(log_dir, exist_ok=True)  # Creates the log directory if it doesn't already exist

# Configures the logging system
logging.basicConfig(
    level=logging.INFO,  # Sets the minimum level of messages to capture (INFO and above)
    format=logging_str,  # Uses the defined log message format
    handlers=[
        logging.FileHandler(log_filepath),  # Writes log messages to a file
        logging.StreamHandler(sys.stdout)  # Also prints log messages to the console (stdout)
    ]
)

logger = logging.getLogger("fraudClassifierLogger")  # Creates a logger instance named 'cnnClassifierLogger'
