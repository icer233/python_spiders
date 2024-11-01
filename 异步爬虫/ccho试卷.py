# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
from multiprocessing.dummy import Pool

# 创建储存目录
if not os.path.exists('./ccho'):
    os.makedirs('./ccho')

url = 'https://ccho.eduzhixin.com/archives/tag/csst/page/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

for i in range(1,4):
    # 创建文件目录实例
    purl = url + str(i)
    response = requests.get(url=purl, headers=headers).text
    tree = etree.HTML(response)
    # 解析div列表
    div_list = tree.xpath('/html/body/div[1]/div[4]/div/div/div[1]/div')
    def down(div):
        detail_url = div.xpath('./article/a[1]/@href')[0] # 获取详情页链接
        name = div.xpath('./article/a[1]/@title')[0]  # 获取文件名
        ans_path = './ccho/' + name +'.pdf' # 生成文件路径
        detail_page = requests.get(url=detail_url, headers=headers).text
        detail_tree = etree.HTML(detail_page)
        try:
            down_url = detail_tree.xpath('//div[@class="row"]/div/article/div/div/div//strong/a/@href')[0]
            data = requests.get(url=down_url, headers=headers).content
            with open(ans_path, 'wb') as fp:
                fp.write(data)
            print(name, 'is downloaded')
        except:
            print('Unable to download', name, ' , url:', detail_url)
    pool = Pool(5)
    pool.map(down, div_list)
    pool.close()
    pool.join()

