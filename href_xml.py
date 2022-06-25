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

items = html.find('li') # look fora <li> main tag (defines a list element)

for a in html.find_all("a"):
    print(a.text)