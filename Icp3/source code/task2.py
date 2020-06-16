import requests
from bs4 import BeautifulSoup
url =  "https://en.wikipedia.org/wiki/Deep_learning"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
"prints the whole html code with clean and indented way"
print(soup.prettify())
"retrives only the title of html without any tags"
title = soup.title.string
print(title)
"finds all the anchore tags in html"
anchortag = soup.find_all('a')
print(anchortag)
"opens the file with write mode "
with open('file2.txt', 'w') as f:
    for link in anchortag:
        "retrives all the href links in the anchore tags"
        href = link.get('href')
        print(href)
        "converts them to string and writes to the file"
        f.write(str(href))
        f.write("\n")

f.close()



