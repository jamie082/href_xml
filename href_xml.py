#/usr/bin/python3

# http://stackabuse/parsing-xml-with-beautifulsoup-in-python/
# https://www.geeksforgeeks.org/beautifulsoup-find-all-li-in-ul/
# https://opensource.com/article/21/9/web-scraping-python-beautiful-soup

import requests
from bs4 import BeautifulSoup

my_site = 'http://sandiego.craigslist.org/search/sof'
data = requests.get(my_site)

my_data = [] # create my_data[] for dataFrame

html = BeautifulSoup(data.text, 'html.parser')

# https://realpython.com/beautiful-soup-web-scraper-python/

results = html.find(class_="rows")

job_elements = results.find_all("div", class_="sortable-results")

for job_element in job_elements:
    element_select = job_element.find("li", class_="result-row")
    print(element_select.text.strip())
    print()