#Done as part of DataCamp Data Science course.

from bs4 import BeautifulSoup
import requests

url = 'https://www.wikipedia.org/'
r = requests.get(url)
html_doc = r.text
#Creates a soup object
soup = BeautifulSoup(html_doc)

#Get Text
print(soup.get_text())

#Get Prettify version of Soup
print(soup.prettify())

#Get Title
print(soup.title)

# Find all 'a' tags (which define hyperlinks) and Print the URLs to the shell
for link in soup.find_all('a'):
    print(link.get('href'))
