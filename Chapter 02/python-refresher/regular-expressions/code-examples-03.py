import re
import random
import string

# Define a regular expression pattern to match valid email addresses
pattern = r"(\w+\.\w+)@(\w+\.\w+)"

# Generate a random first name and last name
first_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
last_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

# Generate a random domain name
domain_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

# Use regular expressions to generate a random email address
email_address = re.sub(pattern, f"{first_name}.{last_name}@{domain_name}.com", "dummy@dummy.com")

# Print the generated email address
print(email_address)
