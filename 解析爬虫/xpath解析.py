# -*- coding:utf-8 -*-
import requests
from lxml import etree

tree = etree.parse('wjx.html')
#r = tree.xpath('/html/body/div')
#r = tree.xpath('/html//div')
#r = tree.xpath('//div[@class='song']')
#r = tree.xpath('//div[@class='song']/p[3]')  索引从1开始
#r = tree.xpath('//div[@class='song']//li[5]/a/text()')[0]
r = tree.xpath('//div[@class='song']/img/@src')[0]
print(r)