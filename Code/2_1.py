#BeautifulSoup 用法
#findAll(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, text ,keywords)
'''
    tag(标签)用法：
    sb.findAll('h1') / sb.findAll('div')
    
    attributes(属性)用法：
    sb.findAll('div', {'id':'TagId'}) 
        可用JSON格式指定属性
    recursive(递归)用法：
    sb.findAll('div', {'class':'TagClass'}, True)
        ①传入参数为布尔值 True 查询标签参数的所有子标签。
        ②一般不需要定义此参数，涉及到抓取速度时考虑。
        ③findAll方法默认为True
    text(文本)用法：
    sb.findAll('div', text = 'the prince')
        抓取包含该文本的标签
    limit(范围限制)用法：
    sb.findAll('div', limit = 7)
        ①抓取符合条件的前n项
        ②find方法实际上是findAll方法将limit设为1时的情况
    keywords(关键词参数)用法：
    sb.find(id = 'TagId')
        选择具体有指定属性的标签

    注意事项：
        因为class在python中是保留字，所以无法使用bs.findAll(class = 'green')。
        若有需求可以在class加'_'，如bs.findAll(class_ = 'green')
'''
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
def getDiv(url) :
    try :
        html = urlopen(url)
    except (HTTPError, URLError) as e :
        print(e)
    try :
        bsObj = BeautifulSoup(html.read(), "html.parser")
        div = bsObj.findAll("div", id="ftCon")
    except AttributeError as e :
        return None
    return div

def getText(url) :
    try :
        html = urlopen(url)
    except (HTTPError, URLError) as e :
        print(e)
    try :
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.findAll("div", id="ftCon")
        for name in nameList :
            print(name.get_text())
    except AttributeError as e :
        return None    

URL = "http://www.baidu.com/"
getText(URL)
 
