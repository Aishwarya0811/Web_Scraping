import urllib.request
from bs4 import *
htmlfile = "https://en.wikipedia.org/wiki/Steve_Jobs?action=edit"
res = requests.get(htmlfile)
res.raise_for_status()
soup = BeautifulSoup(res.text,'html.parser')
soup__ = BeautifulSoup(res.content, 'html.parser')
print(soup.prettify())
soup.find_all('a')
print(soup.get_text())
soup.head.contents
soup.get_text()
paging = soup.find_all("div",{"style":"display:inline"}).find("div",{"id":"paging"}).find_all("a")
web_content_dict["Title"]=item_header.find("a",{"class":"mw-editfont-monospace"})

