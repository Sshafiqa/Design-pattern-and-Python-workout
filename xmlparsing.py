from bs4 import BeautifulSoup

# Sample XML data
xml_data = """
<book>
    <title>Python Programming</title>
    <author>John Doe</author>
    <year>2024</year>
</book>
"""

# Parse XML data
soup = BeautifulSoup(xml_data, 'xml')

# Extract title
title = soup.title.string
print(f"Title: {title}")

# Extract author
author = soup.author.string
print(f"Author: {author}")

# Extract year
year = soup.year.string
print(f"Year: {year}")
