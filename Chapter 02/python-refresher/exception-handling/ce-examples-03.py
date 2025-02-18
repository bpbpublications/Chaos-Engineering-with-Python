# introducing simulated delay
import logging
import time

def perform_operation():
    time.sleep(5) # introduce a simulated delay
    return "Operation completed successfully."

try:
    result = perform_operation()
except Exception as e:
    logging.error(f"An error occurred during the operation: {e}")
    # introduce fallback behavior or alternative paths here
