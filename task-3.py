import requests
from bs4 import BeautifulSoup
url="https://www.bikewale.com/electric-bike/"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
print(soup.text)
print("\nPage Links:\n")
for link in soup.find_all('a', href=True):
    print(link['href'])
print("\n page images:\n")
for img in soup.find_all('img', src=True):
    print(img['src'])