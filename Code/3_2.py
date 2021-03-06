from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

pages = set()
def getLinks(pageUrl) :
    global pages
    html = urlopen("http://en.wikiPedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("little thing")

    for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            # 新页面
            newPage = link.attrs["href"]
            print("----------------\n"+newPage)
            pages.add(newPage)
            getLinks(newPage)
if __name__ == '__main__':
    getLinks("")
