import requests
from bs4 import BeautifulSoup

response = requests.get(
	url="https://en.wikipedia.org/wiki/Albert_Einstein",
)
if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')
    list(soup.children)

    for i in range(1,6):
        print(soup.find_all('p')[i].get_text())

else:
    print("Cannot access website")
