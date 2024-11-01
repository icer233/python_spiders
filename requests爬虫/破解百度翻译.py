# -*- coding:utf-8 -*-
import requests
import json

post_url = 'https://fanyi.baidu.com/sug'
kw = input('input a word: ')
data = {
    'kw': kw
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
response = requests.post(url = post_url, data = data, headers = headers)
dic_obj = response.json()

filepath = './' + kw + '.json'
fp=open(filepath, 'w', encoding = 'utf-8')
json.dump(dic_obj, fp = fp, ensure_ascii = False)

print("saved")