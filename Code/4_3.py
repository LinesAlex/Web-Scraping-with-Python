from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import json
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


def getHistoryIPs(pageUrl):

    pageUrl = pageUrl.replace('/wiki/','')
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, 'html.parser')

    ipAddresses = bsObj.findAll("a",{"class":"mw-userlink mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getLocation(ip) :
    try:
        html = urlopen('http://www.freegeoip.net/json/'+ip)
        response = html.read().decode('utf-8')
    except HTTPError:
        return None
    Json = json.loads(response)
    print('ip : ' + Json.get("ip"))
    print('country_code : ' + Json.get("country_code"))
    print('conutry_name : ' + Json.get("country_name"))
    print('region_code : ' + Json.get("region_code"))
    print('region_name : ' + Json.get("region_name"))
    print('city : ' + Json.get("city"))
    print('zip_code : ' + Json.get("zip_code"))
    print('time_zone : ' + Json.get("time_zone"))
    print('latitude : ' + str(Json.get("latitude")))
    print('longitude : ' + str(Json.get("longitude")))
    print('metro_code : ' + str(Json.get("metro_code")))
    print('———————')
    return Json.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")
while(len(links) > 0):
    for link in links:
        print("------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            getLocation(historyIP)
    newLink = links[reandom.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)
