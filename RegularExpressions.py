# Example 1
pattern = r'(\d{4})-(\d{2})-(\d{2})'  # Matches YYYY-MM-DD
text = "The date is 2023-09-28"

# Search for the date pattern
match = re.search(pattern, text)
if match:
    print("Year:", match.group(1))  # First group
    print("Month:", match.group(2))  # Second group
    print("Day:", match.group(3))  # Third group

# Example 2
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
text = "The date is 2023-09-28"

# Search with named groups
match = re.search(pattern, text)
if match:
    print("Year:", match.group('year'))
    print("Month:", match.group('month'))
    print("Day:", match.group('day'))

# Example 3
pattern = r'(?:http|https)://(\w+\.\w+)'
text = "Visit http://example.com or https://example.org"

# Find all domain names
matches = re.findall(pattern, text)
print("Domains:", matches)

# Example 4
pattern = r'\w+(?=\sis)'  # Match word followed by " is"
text = "Python is powerful and regex is fun"

matches = re.findall(pattern, text)
print("Lookahead matches:", matches)


# Example 5
pattern = r'(?<=is\s)\w+'  # Match word preceded by "is "
text = "Python is powerful and regex is fun"

matches = re.findall(pattern, text)
print("Lookbehind matches:", matches)



