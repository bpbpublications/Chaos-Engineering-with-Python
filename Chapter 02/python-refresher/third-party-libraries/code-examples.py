import requests

def simulate_network_timeout():
    url = "https://example.com"
    try:
        response = requests.get(url, timeout=0.001)
    except requests.exceptions.Timeout:
        print("Network timeout occurred")
