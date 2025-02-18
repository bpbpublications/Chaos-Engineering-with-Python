import re

text = "The quick brown fox jumps over the lazy dog."
pattern = "fox"

# Search for the pattern in the text
match = re.search(pattern, text)

# Print the matched text and its position
if match:
    print(f"Matched '{match.group()}' at position {match.start()}-{match.end()}.")
else:
    print("No match found.")
