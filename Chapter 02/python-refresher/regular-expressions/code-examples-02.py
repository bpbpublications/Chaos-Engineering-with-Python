import re

# Define a regular expression pattern to match error codes and IP addresses
pattern = r"Error (\d+): IP address (\d+\.\d+\.\d+\.\d+)"

# Open the log file and read its contents
with open("logfile.txt", "r") as f:
    contents = f.read()

# Use regular expressions to extract error codes and IP addresses from the log file
matches = re.findall(pattern, contents)

# Print the extracted information
for error_code, ip_address in matches:
    print(f"Error {error_code} occurred at IP address {ip_address}")
