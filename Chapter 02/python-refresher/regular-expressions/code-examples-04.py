
import re

# Define a regular expression pattern to match valid email addresses
pattern = r"^\w+[\w\.-]*@\w+[\w\.-]+\.\w{2,4}$"

# Ask the user to enter their email address
email = input("Enter your email address: ")

# Use regular expressions to validate the email address
if re.match(pattern, email):
    print("Email address is valid")
else:
    print("Email address is not valid")
