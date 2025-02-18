# introduce a random failure
import logging
import random

def perform_operation():
    if random.random() < 0.5:
        raise Exception("Something went wrong during the operation.")
    else:
        return "Operation completed successfully."

try:
    result = perform_operation()
except Exception as e:
    logging.error(f"An error occurred during the operation: {e}")
    # introduce fallback behavior or alternative paths here
