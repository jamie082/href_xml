#/usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = 'http://sandiego.craigslist.org/search/sof'
req =  requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

urls = []
for h in soup.find_all('a'):
    print(h.get('href'))