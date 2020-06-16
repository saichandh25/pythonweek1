import requests
from bs4 import BeautifulSoup
url =  "https://en.wikipedia.org/wiki/Deep_learning"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())
title = soup.title.string
print(title)
anchortag = soup.find_all('a')
print(anchortag)
with open('file2.txt', 'w') as f:
    for link in anchortag:
        href = link.get('href')
        print(href)
        f.write(str(href))
        f.write("\n")

f.close()



