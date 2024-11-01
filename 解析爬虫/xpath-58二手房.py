# -*- coding:utf-8 -*-
import requests
from lxml import etree

url = 'https://bj.58.com/ershoufang/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
div_list = tree.xpath('//section[@class="list"]/div')
fp = open('58.txt', 'w', encoding='utf-8')
for div in div_list:
    title = div.xpath('./a//div[2]//div/h3/text()')[0]
    print(title)
    fp.write(title + '\n')
