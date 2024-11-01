# -*- coding:utf-8 -*-
import requests
from lxml import etree

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

page_text = requests.get(url=url, headers=headers,verify=False).text
tree = etree.HTML(page_text)
all_city_names = []

# 所有城市里包含了热门城市
# 单独解析热门城市：
# hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
# for li in hot_li_list:
#     hot_city_name = li.xpath('./a/text()')[0]
#     all_city_names.append(hot_city_name)

all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
for li in all_li_list:
    city_name = li.xpath('./a/text()')[0]
    all_city_names.append(city_name)

print(all_city_names, len(all_city_names))