#/usr/bin/python3

# http://stackabuse/parsing-xml-with-beautifulsoup-in-python/
# https://www.geeksforgeeks.org/beautifulsoup-find-all-li-in-ul/
# https://opensource.com/article/21/9/web-scraping-python-beautiful-soup

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

my_site = 'http://sandiego.craigslist.org/search/sof'
data = requests.get(my_site)

my_data = [] # create my_data[] for dataFrame

html = BeautifulSoup(data.text, 'html.parser')

items = html.find('ul') # look fora <li> main tag (defines a list element)

# https://realpython.com/beautiful-soup-web-scraper-python/

<div id="sortable-results">
    <--all the job listings -->
</div>

results = html.find(id="sortable-resuls")

job_elements = results.find_all("li")

for job_element in job_elements:
    element_select = job_element.find("li", class_="result-row")
    print(element_select.text.strip())
    print()