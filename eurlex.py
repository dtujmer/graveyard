from google import google
from bs4 import BeautifulSoup
import requests
import re


num_page = 1
search_item = raw_input("Search EUR-Lex >>> ")
query = search_item + " eurlex"
search_results = google.search(query, num_page)

eurlex_link_EN = search_results[0].link.replace("/HR/TXT/", "/EN/TXT/HTML/")
eurlex_link_HR = search_results[0].link.replace("/HR/TXT/", "/HR/TXT/HTML/")

print eurlex_link_EN
print eurlex_link_HR



r1 = requests.get(eurlex_link_EN)
soup1 = BeautifulSoup(r1.content, "lxml")

r2 = requests.get(eurlex_link_HR)
soup2 = BeautifulSoup(r2.content, "lxml")


found_string = soup2.find(string=re.compile(search_item))
print found_string

# how you would locate the exact tag is the following process:
# 1. measure how many tags this one is from its first parent
# 2. measure the number of tags of the parent to its parent.
# 3. repeat recursively up to the point of the /body tag
# 4. you will have a series of numbers you have to retrace on the second text
# 5. retrace these numbers and you have your tag, which means that you have your segment
