#/usr/bin/python3

# http://stackabuse/parsing-xml-with-beautifulsoup-in-python/
# https://www.geeksforgeeks.org/beautifulsoup-find-all-li-in-ul/

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://sandiego.craigslist.org/search/sof'
req =  requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

# create DataFrame

df = pd.DataFrame(columns=['href', 'result-hood', 'datetime']) # create columns


for item in soup.find_all("li"): # create element ordered list
    href_output = item.find('href')
    location_obj = item.find('result-hood')
    time_obj = item.find('datetime')

    urls = []

    row = {
        'columns': href_output,
        'href': location_obj,
        'time': time_obj
    }

    df = pd.DataFrame(row)

print(df)


# output a href list into Description, Location and Time columns (html.parser)