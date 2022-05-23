#/usr/bin/python3

# stackabuse/parsing-xml-with-beautifulsoup-in-python/

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://sandiego.craigslist.org/search/sof'
req =  requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

# create DataFrame

df = pd.DataFrame(columns['Description'])

urls = []
for h in soup.find_all('a'):
    print(h.get('href'))

    row = {
        'columns': h,
    }

    df = df.append(row, ignore_index=True)
    print(f'Appending row %s of %s' % (index+1, items_length))

print(df)