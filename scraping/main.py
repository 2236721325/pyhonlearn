import requests
from lxml import etree
from lxml.etree import _Element
indexUrl="http://www.2552.com.cn/shi/"
response=requests.get(indexUrl)
html=response.content.decode("utf-8")
result:_Element=etree.HTML(html)

    
nodes:list[_Element]=result.xpath("//div[@class='card-body']")
for j in range(nodes.__len__()-2):
    title=nodes[j].xpath("")
import requests

indexUrl="http://www.2552.com.cn/shi/"
response=requests.get(indexUrl)
html=response.content.decode("utf-8")
print(html)



def getNums()->any:
    return [1,2,3,4]

l=getNums()
