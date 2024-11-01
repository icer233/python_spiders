import requests
from multiprocessing.dummy import Pool
from lxml import etree
import re
import os

if not os.path.exists('./vids'):
    os.makedirs('./vids')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}
url = 'https://pearvideo.com/category_5'
page_text = requests.get(url=url, headers=headers).text

tree=etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
urls = []
for li in li_list:
    detail_url ='https://pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    detail_text = requests.get(url=detail_url, headers=headers).text
    # 没法找mp4链接了 ex = 'src="(https://video.pearvideo.com/mp4/.*?\.mp4")'
    vid_url = re.findall(ex, detail_text, re.S)[0]
    dic = {
        'name': name,
        'url': vid_url
    }
    urls.append(dic)

def getVid(dic):
    url = dic['url']
    path = './vids/' + dic['name']
    print(dic['name'], 'downloading......')
    data =requests.get(url=url, headers=headers).content
    with open(path, 'wb') as fp:
        fp.write(data)
        print(dic['name'], 'saved!')

pool = Pool(4)
pool.map(getVid, urls)

pool.close()
pool.join()