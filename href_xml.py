#/usr/bin/python3

# http://stackabuse/parsing-xml-with-beautifulsoup-in-python/

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://sandiego.craigslist.org/search/sof'
req =  requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

# create DataFrame

df = pd.DataFrame(columns=['href', 'result-hood', 'datetime']) # create columns

this_var = soup.find_all('li')
#h = soup.find('href').text
#for h, item in soup.find_all('li'):
for index, item in enumerate(this_var):
    href_output = item.find('href').text
    location_obj = item.find('result-hood').text
    time_obj = item.find('datetime').text

    a = h.find('a')
    urls.append(a.attrs['href'])

    row = {
        'columns': href_output,
        'href': location_obj,
        'time': time_obj
    }

    df = df.append(href_output, ignore_index=True)
    print(f'Appending row %s of %s' % (index+1, items_length))

print(df)


# output a href list into Description, Location and Time columns (html.parser)