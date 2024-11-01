# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}
fp = open('./wjx.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'lxml')
print(soup.find('span'))