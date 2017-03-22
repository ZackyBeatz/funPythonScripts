from bs4 import BeautifulSoup
import requests

#  FUN SCRIPT THAT CRAWLS THROUGH A WEB DOCUMENT WITH BEAUTIFULSOUP
# check BeautifulSoup Docs for all information
r = requests.get("http://example.com/")

soup = BeautifulSoup(r.text, 'lxml')



# gets all a href links
allLinks = soup.find_all('a')

# gets h1 within body 
head1 = soup.body.h1

# gets same h1 without title attribute
headWTitle = soup.body.h1.string



# gets document title
getDocumentTitle = soup.title


print(headWTitle)