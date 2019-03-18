import requests
import re
from lxml import etree
import io

# Pick the original language

print('Language codes:\nen: English\nde: German\nfr: French\netc.')
lang1 = input('Enter language code >> ')

# Enter the searched term, then replace the whitespace with '+'.
# The reason is because whitespace isn't supported when passed in URL.

query = input('Enter the search term >> ')
if ' ' in query:
    query = query.replace(' ', '+')
	
# GET the search results page for the term and language.

r = requests.get(('https://eur-lex.europa.eu/search.html?&text="{}"'
    '&scope=EURLEX&type=quick&lang={}').format(query, lang1))
	
# Build a list of regex matches for links to individual legal texts.

reg1 = re.findall((r'(legal-content\/[\/?=:0-9a-zA-Z]*)'
    '&amp;[\/?=:0-9a-zA-Z]*"'), r.text)
	
	
# Idea: remove duplicates while preserving order of search results!
# This means that normal set() won't work (mixes up the results).

# Replace 'PDF' with 'HTML' and combine with https://eur-lex.europa.eu/
# then build a list of such URLs.

root = 'https://eur-lex.europa.eu/'
reg2 = [root + i.replace('PDF', 'HTML') for i in reg1]

# GET the first result and its translation


z1 = requests.get(reg2[0])
z2 = requests.get(reg2[0].replace('EN', 'HR'))

# soup1 = BeautifulSoup(z1.content, 'html.parser')
# soup2 = BeautifulSoup(z2.content, 'html.parser')

# with open('out1.xml', 'w', encoding='utf-8') as a:
    # a.write(soup1.prettify())
	
# with open('out2.xml', 'w', encoding='utf-8') as b:	
    # b.write(soup2.prettify())

# YOU NEED AN XML PARSER, NOT HTML! THE RESPONSE FROM EURLEX IS XML!

# Consider not using .xml files but strings instead.

# You will find the index of an xml segment by [any list].index('segment')

# Research serverless architecture for this project

# Include GTranslate and highlight str if it matches with GTranslate

# Use lxml. Then, use either getpath or xpath - one of them will allow
# you to find the query and return its path. With that info, you can
# then return the parallel result (target text).


# You will need two xpath expressions - one to locate the right node,
# another to GETPATH of that node. So 1st xpath returns the node, second
# expression returns the path of that node, 3rd expression passes this
# to another function (for the target text).

doc = z1.text


with open("document.xml", "w", encoding='utf-8') as document:
    document.write(doc)
	
data = open("document.xml")

tree_content = data.read()

root = etree.XML(tree_content)

x = tree_content.xpath("//p[contains(., query)]")
print(tree.getpath(x))
