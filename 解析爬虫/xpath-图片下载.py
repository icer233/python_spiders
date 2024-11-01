# -*- coding:utf-8 -*-
import requests
from lxml import etree
import re
import os

if not os.path.exists('./piclib'):
    os.makedirs('./piclib')

url = 'https://pic.netbian.com/4kyouxi/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
for li in li_list:
    img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
    img_name = re.findall('.*?allimg/.*?/(.*?\.jpg)', img_src)[0]
    #img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    #img_name = img_name.encode('utf-8').decode('latin 1')
    #print(img_name, img_src)
    img_data = requests.get(url=img_src, headers=headers).content
    img_path = './piclib/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, 'downloaded')
