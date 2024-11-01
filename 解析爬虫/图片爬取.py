# -*- coding:utf-8 -*-
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
url = 'https://tse2-mm.cn.bing.net/th/id/OIP-C.H3xxELTo78yG8EyUw54PBAAAAA?rs=1&pid=ImgDetMain'
img_data = requests.get(url = url).content

with open('./解析爬虫/test.jpg', 'wb') as fp:
    fp.write(img_data)