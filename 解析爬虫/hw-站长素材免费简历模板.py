# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

if not os.path.exists('./jianli'):
    os.makedirs('./jianli')

url = 'https://sc.chinaz.com/jianli/free.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

page_text = requests.get(url=url, headers=headers).content
tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@id="main"]/div[1]/div')

for div in div_list:
    detail_url = div.xpath('./a/@href')[0]
    detail_response = requests.get(url=detail_url, headers=headers)
    detail_response.encoding = 'utf-8'
    detail_text = detail_response.text
    detail_tree = etree.HTML(detail_text)
    down_url = detail_tree.xpath('//div[@class="down_wrap"]/div[2]/ul/li[1]/a/@href')[0]
    name = detail_tree.xpath('//div[@class="bggray clearfix"]/div[2]/div[2]//h1//text()')[0]
    jianli_path = './jianli/' + name + '.rar'
    data = requests.get(url=down_url, headers=headers).content
    with open(jianli_path, 'wb') as fp:
        fp.write(data)
    print(name, '已下载')

print('over')
    