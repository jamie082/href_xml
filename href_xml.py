#/usr/bin/python3

# http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/

import requests
from bs4 import BeautifulSoup

url = 'http://sandiego.craigslist.org/search/sof'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

urls = []
for h in soup.find_all('li'):
    a = h.find('a')
    urls.append(a.attrs['href'])