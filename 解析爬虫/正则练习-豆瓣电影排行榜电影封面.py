# 练习爬取豆瓣电影排行榜电影封面
# -*- coding:utf-8 -*-
import requests
import re
import os

if not os.path.exists('./movie_covers'):
    os.makedirs('./movie_covers')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
url = 'https://movie.douban.com/chart'

page_text = requests.get(url=url, headers=headers).text
ex='<a class="nbg" href=.*?<img src="(.*?)" width="75" alt=.*?</a>'
img_src_list = re.findall(ex, page_text, re.S)

for src in img_src_list:
    img_data = requests.get(url=src, headers=headers).content
    img_name = re.findall('/public/(.*?\.jpg)', src)[0]
    img_path = './movie_covers/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, 'downloaded!\n')

print('over')