from bs4 import BeautifulSoup
import requests

# URL of the e-commerce site
url = 'https://www.example.com/products'

# Fetch the content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract and print product names and prices
products = soup.find_all('div', class_='product')
for product in products:
    name = product.find('h2').get_text()
    price = product.find('span', class_='price').get_text()
    print(f"Product: {name}, Price: {price}")
