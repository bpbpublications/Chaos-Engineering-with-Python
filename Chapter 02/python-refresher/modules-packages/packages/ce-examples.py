import requests
import chaos_tools.network as network

# Simulate network latency for requests to the API endpoint
with network.latency(delay=500, jitter=50):
    response = requests.get('http://myapi.com/users')
    print(response.json())
