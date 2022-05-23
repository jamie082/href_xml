#/usr/bin/python3

# http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/
# https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm

import requests
from bs4 import BeautifulSoup

url = 'http://sandiego.craigslist.org/search/sof'
req =  requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

urls = []
for h in soup.find_all('a'):
    print(h.get('href'))