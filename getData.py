from bs4 import BeautifulSoup
import requests

r = requests.get("http://example.com/")

soup = BeautifulSoup(r.text, 'lxml')


print(soup.prettify())