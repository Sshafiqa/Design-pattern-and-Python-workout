from bs4 import BeautifulSoup
import requests

# Fetch HTML content from a web page
response = requests.get('https://www.example.com')
html_content = response.text

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract title
title = soup.title.string
print(f"Title of the page: {title}")

# Extract all paragraph texts
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())
