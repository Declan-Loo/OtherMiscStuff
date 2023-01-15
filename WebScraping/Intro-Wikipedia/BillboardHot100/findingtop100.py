import requests
from bs4 import BeautifulSoup
 
page = requests.get('https://www.billboard.com/charts/hot-100/') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

table = soup.find_all('div', class_ = 'o-chart-results-list-row-container') 
print("CURRENT BILLBOARD HOT 100 RANK [According to https://www.billboard.com/charts/hot-100/ ]")

artists = soup.find('span', class_ = 'c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')


for i in range(1,len(table)+1):
  print(str(i)+".", end="")
  print(table[i-1].h3.text.strip())
  
#TODO: artists of each song (currently it only prints the song titles).
