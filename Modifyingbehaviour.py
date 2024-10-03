# Example 1
pattern = r'python'
text = "I love PYTHON programming"

match = re.search(pattern, text, re.IGNORECASE)
print("Case-insensitive match:", match.group())

# Example 2
pattern = r'^hello'
text = """hello world
this is a test
hello again"""

matches = re.findall(pattern, text, re.MULTILINE)
print("Multiline matches:", matches)

# Example 3
pattern = r'<.*>'  # Match everything between < and >
text = "<div>content</div>"

match = re.search(pattern, text)
print("Greedy match:", match.group())

# Example 4
pattern = r'<.*?>'  # Match as little as possible between < and >
text = "<div>content</div>"

match = re.search(pattern, text)
print("Non-greedy match:", match.group())

# Example 5
pattern = re.compile(r'\d+')

# Search for numbers
text = "There are 3 apples and 10 bananas"
matches = pattern.findall(text)
print("Matches:", matches)

# Example 6
pattern = re.compile(r'''
    (\d{4})  # Match 4 digits (year)
    -        # Hyphen
    (\d{2})  # Match 2 digits (month)
    -        # Hyphen
    (\d{2})  # Match 2 digits (day)
''', re.VERBOSE)

text = "Today's date is 2023-09-28"
match = pattern.search(text)
if match:
    print("Year:", match.group(1))
    print("Month:", match.group(2)

# Example 7


    def replace_year(match):
        year = int(match.group())
        return str(year + 1)


    pattern = r'\d{4}'
    text = "The year is 2023"

    # Increment the year by 1
    new_text = (re.sub(pattern, replace_year, text)
    print("Updated text:", new_text)


