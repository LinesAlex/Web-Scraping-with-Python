import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
def useRe():
    string = '''Who has seen the wind? Neither I nor you;But when the leaves hang trembling,
The wind is passing through.Who has seen the wind?Neither you nor I;
But when the trees bow down their heads,The wind is passing by.
——Christina Rossetti'''
    R1 = re.search('seen', string)
    print(R1.span())
    R2 = re.match('Who', string)
    print(R2.span())
    R3 = re.split(',', string)
    for s in R3 :
        print(s)
    R4 = re.findall('t', string)
    print(len(R4))
    R5 = re.sub(';', '.', string)
    print(R5)
    
def findImage(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html,'html.parser')
    images = bsObj.findAll("img", {'src':re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    for image in images:
        print(image['src'])
    #lambda
    tag = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
if __name__ == '__main__' :
    useRe()
    findImage('http://www.baidu.com/')


    
