import requests
import threading
import logging
import time

def send_request():
    url = 'http://localhost:5000/products'
    start_time = time.time()  # Capture the start time
    response = requests.get(url)
    end_time = time.time()  # Capture the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    logging.info(f'Response: {response.status_code}, Elapsed Time: {elapsed_time:.2f} seconds')

if __name__ == '__main__':
    # Basic logging configuration
    logging.basicConfig(filename='traffic.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Simulate traffic by sending multiple requests in parallel
    for i in range(1000):
        t = threading.Thread(target=send_request)
        t.start()
