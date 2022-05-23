#/usr/bin/python3

# http://stackabuse/parsing-xml-with-beautifulsoup-in-python/

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://sandiego.craigslist.org/search/sof'
req =  requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

# create DataFrame

df = pd.DataFrame(columns=['Description', 'Location', 'Time'])

urls = []
for h, item in soup.find_all('li'):
    href_output = item.find('href')
    location = item.find('result-hood')
    time_of = item.find('datetime')

    #print(h.get('href'))

    #h = soup.find('href').text
    a = h.find('a')
    urls.append(a.attrs['href'])

    row = {
        'columns': href_output,
    }

    df = df.append(href_output, ignore_index=True)
    print(f'Appending row %s of %s' % (index+1, items_length))

print(df)