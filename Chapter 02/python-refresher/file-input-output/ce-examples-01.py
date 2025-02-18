import random

# Generate random latency values
latency_values = [random.randint(0, 1000) for _ in range(10)]

# Write the values to a file
with open('latency_results.txt', 'w') as f:
    for value in latency_values:
        f.write(str(value) + '\n')
