import sys
from src.fraudClassifier import logger
from src.fraudClassifier.exception import CustomException

logger.info("This is an info message from the main module.")

try:
    1 / 0
except Exception as e:
    raise CustomException(e)