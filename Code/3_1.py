from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
def test():
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
            if 'href' in link.attrs:
                print(link.attrs['href'])
random.seed(datetime.datetime.now())
def getLinks(artUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
pages = set()
def getUniqueLinks(url):
    global pages
    html = urlopen("http://en.wikipedia.org" + url)
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages :
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getUniqueLinks(newPage)
                
if __name__ == '__main__':
    getUniqueLinks("")
    links = getLinks("/wiki/Kevin_Bacon")
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
    
