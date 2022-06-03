#/usr/bin/python3

# http://stackabuse/parsing-xml-with-beautifulsoup-in-python/
# https://www.geeksforgeeks.org/beautifulsoup-find-all-li-in-ul/
# https://opensource.com/article/21/9/web-scraping-python-beautiful-soup

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

df = pd.DataFrame(columns=['result-hood', 'datetime']) # create columns

my_site = 'http://sandiego.craigslist.org/search/sof'
data = requests.get(my_site)

my_data = [] # create my_data[] for dataFrame

html = BeautifulSoup(data.text, 'html.parser')

items = html.select('li')

for item in items: # create element ordered list
    # new objectss
    per_1 = item.select('a') # save a href links

    my_data.append({"per_1": per_1}) # only one item, <a href links

pprint(per_1)

"""
    row = {
        #'columns': href_output,
        'href': location_obj,
        'time': time_obj
    }

    df = pd.DataFrame(row, index=[0, 1, 2, 3])

print(df)

"""
# output a href list into Description, Location and Time columns (html.parser)