import os

def simulate_process_crash():
    pid = os.getpid()
    os.kill(pid, 9)
