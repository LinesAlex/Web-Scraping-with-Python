from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

def getLocation(ip) :
    html = urlopen('http://www.freegeoip.net/json/'+ip)
    response = html.read().decode('utf-8')
    print(response)
    Json = json.loads(response)
    print('ip : ' + Json.get("ip"))
    print('country_code : ' + Json.get("country_code"))
    print('conutry_name : ' + Json.get("country_name"))
    return Json.get("country_code")

if __name__ == "__main__" :
    print(getLocation('120.43.37.122'))
