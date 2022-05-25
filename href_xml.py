#/usr/bin/python3

# http://stackabuse/parsing-xml-with-beautifulsoup-in-python/
# https://www.geeksforgeeks.org/beautifulsoup-find-all-li-in-ul/
# https://opensource.com/article/21/9/web-scraping-python-beautiful-soup

import requests
from bs4 import BeautifulSoup
import pandas as pd

my_site = 'http://sandiego.craigslist.org/search/sof'
data = requests.get(my_site)

html = BeautifulSoup(data.text, 'html.parser')
items = html(select('li'))

# create DataFrame

df = pd.DataFrame(columns=['result-hood', 'datetime']) # create columns

html = BeautifulSoup(data.text, 'html.parser')
items = html.select('li')

for item in items: # create element ordered list
    #href_output = item.find('href')
    location_obj = item.find('result-hood').text()
    time_obj = item.find('datetime').text()

    urls = []

    row = {
        #'columns': href_output,
        'href': location_obj,
        'time': time_obj
    }

    df = pd.DataFrame(row, index=[0, 1, 2, 3])

print(df)


# output a href list into Description, Location and Time columns (html.parser)