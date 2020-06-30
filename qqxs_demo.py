
import requests
from lxml import etree

url = "https://www.qqxsnew.com/43/43475/"
response = requests.get(url)
#print(response.text)
dom = etree.HTML(response.text)
nodes = dom.xpath('//dl/dd[position()>12]')
#print(nodes)
for node in nodes:
    #print(node)
    title = node.xpath("./a/text()")[0]
    new_url = 'https://www.qqxsnew.com' + node.xpath("./a/@href")[0]
    #print(new_url)
    content = requests.get(new_url)
    result = etree.HTML(content.text).xpath('//div[@id="content"]/text()')
    for i in result:
        #print(i)
        with open("陆鸣陆瑶/" + title + ".txt", "a", encoding="utf-8") as f:
            f.write(i + "\n")


