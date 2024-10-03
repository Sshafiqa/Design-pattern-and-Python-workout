# Example 1
import re

pattern = r'hello'
text = "hello world"

# Match at the beginning of the string
match = re.match(pattern, text)
if match:
    print("Matched:", match.group())

# Example 2
pattern = r'world'
text = "hello world"

# Search for pattern anywhere in the string
search = re.search(pattern, text)
if search:
    print("Found:", search.group())

#Example3
pattern = r'\d+'  # Match one or more digits
text = "The year 2023 is followed by 2024"

# Find all occurrences of the pattern
matches = re.findall(pattern, text)
print("All matches:", matches)

# Example 4
pattern = r'\s+'  # Split by any whitespace
text = "Split this sentence into words"

# Split the string based on pattern
split_text = re.split(pattern, text)
print("Splitted:", split_text)

# Example 5
pattern = r'\d{4}'  # Match any 4-digit number
text = "The year is 2023, soon it will be 2024"

# Replace the pattern with a new value
new_text = re.sub(pattern, "XXXX", text)
print("Replaced text:", new_text)
