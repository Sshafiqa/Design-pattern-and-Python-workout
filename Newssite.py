from bs4 import BeautifulSoup
import requests

# URL of the news site
url = 'https://news.ycombinator.com/'

# Fetch the content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print news headlines
headlines = soup.find_all('a', class_='storylink')
for headline in headlines:
    print(headline.get_text())
