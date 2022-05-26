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

html = BeautifulSoup(data.text, 'html.parser')
items = html.select('li')

my_data = [] # create my_data[] for dataFrame

for item in items: # create element ordered list
    # new objectss
    result_hood = item.select('result-hood')
    item = item.select('datetime')

    my_data.append({"title": result_hood, "item": item})

pprint(my_data)

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