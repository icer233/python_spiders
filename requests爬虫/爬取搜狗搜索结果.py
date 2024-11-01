# -*- coding:utf-8 -*-
import requests

def spi1():
    url = 'https://www.sogou.com/web'
    param = {
        'query': kw
    }
    response = requests.get(url = url, params = param, headers = headers)
    page_text = response.text
    filename=kw + '.html'
    with open(filename, 'w', encoding = 'utf-8') as fp:
        fp.write(page_text)
    print(filename, "保存成功")

def spi2():
    url = 'https://www.sogou.com/web?query='
    
    response = requests.get(url = url + kw, headers = headers)
    page_text = response.text
    filename=kw + '.html'
    with open(filename, 'w', encoding = 'utf-8') as fp:
        fp.write(page_text)
    print(filename, "保存成功")

kw = input('enter a key word : ')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
spi2()