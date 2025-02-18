# example code
import random, time

def send_request_to_database():
    if check_database_availability():
        # send request to database
        return "Success"
    else:
        # introduce chaos by randomly delaying response or returning error code
        delay = random.randint(1, 5)
        time.sleep(delay)
        return "Error"

def check_database_availability():
    # code to check if database is available 
    return # return True if available, False if not
