from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
def getTitle(url) :
    try :
        html = urlopen(url)
    except (HTTPError, URLError) as e :
        print(e)
    try :
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.div
    except AttributeError as e :
        return None
    return title
title = getTitle("http://www.baidu.com/")
if title is None :
    print("Title could not be found")
else :
    print(title)
