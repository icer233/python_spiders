# -*- coding:utf-8 -*-
import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type': '24', # 喜剧
    'interval_id': '100:90',
    'action': '',
    'start': '0', # 从第几部开始
    'limit': '20' # 一次取出几个
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

response = requests.get(url = url, params = param, headers = headers)
list_data = response.json()

fp = open('./douban.json', 'w', encoding = 'utf-8')
json.dump(list_data, fp = fp, ensure_ascii = False)

print('saved')