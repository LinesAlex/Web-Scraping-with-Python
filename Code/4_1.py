from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

def getLocation(ip) :
    html = urlopen('http://www.freegeoip.net/json/'+ip)
    response = html.read().decode('utf-8')
    Json = json.loads(response)
    for key,value in Json.items() :
        print(key + " : " + str(value))
    return Json["country_code"]

if __name__ == "__main__" :
    getLocation('120.43.37.122')
