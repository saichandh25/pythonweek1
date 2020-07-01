
import requests
from bs4 import BeautifulSoup
url=requests.get("https://en.wikipedia.org/wiki/Google")
prety=BeautifulSoup(url.content, "html.parser")

data = prety.body.get_text()
datalines = [i.strip() for i in data.splitlines()]
data_chunk = [word.strip() for line in datalines for word in line.split(" ")]
text = ' '.join(chunk for chunk in data_chunk if chunk)
file=open("texts.txt","a+")
file.write(str(text.encode("utf-8")))
file.close()
print("written")