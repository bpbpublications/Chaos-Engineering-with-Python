import random
import time

class Latency:
    def __init__(self, delay, jitter):
        self.delay = delay
        self.jitter = jitter
        
    def __enter__(self):
        time.sleep((self.delay / 1000) + random.uniform(-(self.jitter / 1000), (self.jitter / 1000)))
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def latency(delay, jitter):
    return Latency(delay, jitter)
