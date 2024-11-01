# -*- coding:utf-8 -*-
import requests
import json
url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
keyword = input('enter a keyword: ')
data = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': '1',
    'pageSize': '10'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

response = requests.post(url = url, data = data, headers = headers )
result = response.json()

# get sum store number
cnt = result['Table']
cnt = cnt[0]
cnt = cnt['rowcount']
data['pageSize'] = cnt

full_result = requests.post(url = url, data = data, headers = headers ).json()

filepath = './' + keyword + ".json"
fp = open(filepath, 'w', encoding = 'utf-8')
json.dump(full_result, fp = fp, ensure_ascii = False)


print('saved')