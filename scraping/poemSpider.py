import requests
from lxml import etree
from lxml.etree import _Element
# 编码检测
# http://www.mytju.com/classcode/tools/messyCodeRecover.asp
indexUrl="http://www.2552.com.cn/shi/"
for i in range(1,100):
    print(f"第{i}页")
    url=indexUrl
    if(i>1):
        url+=f"index_{i}.html"
    response=requests.get(url)
    content=response.content.decode('utf-8')

    result:_Element=etree.HTML(content)

    print("------------------------------------------------------------------------------------------------------------------------")
    nodes:list[_Element]=result.xpath("//div[@class='card-body']")
    for j in range(nodes.__len__()-2):
        title:list[_Element]=nodes[j].xpath(".//h1[@class='h3 fw400']/a")
        author:list[_Element]=nodes[j].xpath(".//a[@href='/']")
        body:list[_Element]=nodes[j].xpath("div[@class='article_show_content lh30 common-content']")
        print(title[0].text)
        print()
        print("------",author[0].text)
        print(etree.tostring(body[0],encoding='utf-8',method='text').decode('utf-8'))
        print("\n\n\n")
        print("------------------------------------------------------------------------------------------------------------------------")


def getNums()->any:
    return [1,2,3,4]
    
nums:list[int]=getNums()

