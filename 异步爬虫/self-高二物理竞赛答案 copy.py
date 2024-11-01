# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
import re
from multiprocessing.dummy import Pool
import unicodedata

# 创建储存目录
if not os.path.exists('./phy'):
    os.makedirs('./phy')

url = 'http://sh.gaokao.com/gzjs/gewl/gewlst/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

# 创建文件目录实例
response = requests.get(url=url, headers=headers, timeout=120)
response.encoding = 'gb2312'
page_text = response.text
tree = etree.HTML(page_text)

# 输出对齐需要的函数
width = 68
def get_display_width(text):
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in 'WF':
            width += 2
        else:
            width += 1
    return width

def format_text(text, width):
    display_width = get_display_width(text)
    padding = width - display_width
    return text + ' ' * padding

# 解析li列表
li_list = tree.xpath('//div[@id="main"]//ul[@class="text_list1"]/li')
def down(li):
    detail_url = li.xpath('./div[@class="title"]/a/@href')[0] # 获取详情页链接
    name = li.xpath('./div[@class="title"]/a/text()')[0]  # 获取文件名
    ans_path = './phy/' + name +'.rar' # 生成文件路径
    
    if not os.path.exists(ans_path):
        # 获取文件下载链接
        print(f"{format_text(name, width)}\t\033[0;36m\033[1m获取下载链接......\033[0m")
        detail_text = requests.get(url=detail_url, headers=headers, timeout=300).text
        down_url = re.findall('(http://files\.eduuu\.com/ohr/.*?\.rar)|(http://files\.eduu\.com/down\.php\?id=288283)', detail_text, re.S)[0] # 发现每个页面框架不一样，但是只有一个rar文件, 第14届的要特判
        if down_url[0]:
            down_url = down_url[0]
        else:
            down_url = down_url[1]
        print(f"{format_text(name, width)}\t\033[0;32m\033[1m成功获取下载链接！\033[0m")

        # 下载并保存rar文件
        print(f"{format_text(name, width)}\t\033[0;36m\033[1m开始下载......\033[0m")
        data = requests.get(url=down_url, headers=headers, timeout=180).content
        with open(ans_path, 'wb') as fp:
            fp.write(data)
            print(f"{format_text(name, width)}\t\033[0;32m\033[1m下载成功！\033[0m")
    else:
        print(f"{format_text(name, width)}\t\033[0;35m\033[1m已存在！\033[0m")

temp_txt = '\033[0;37m\033[1m文件\033[0m'
print(f"{format_text(temp_txt, 85)}\t\033[0;34m\033[1m状态\033[0m")
pool = Pool(10)
pool.map(down, li_list)

pool.close()
pool.join()

print('\n\033[0;32m\033[1m\033[4m全部下载完成！\033[0m')