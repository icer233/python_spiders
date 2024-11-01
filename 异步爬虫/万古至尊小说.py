# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
from multiprocessing.dummy import Pool

def create_path(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

book_url = 'https://www.bqvvxg8.cc/wenzhang/1/1424/' + 'index.html'
book_detail_content = requests.get(url=book_url, headers=headers)
book_detail_content.encoding = 'gbk'
book_detail_content = book_detail_content.text
book_detail_tree = etree.HTML(book_detail_content)
book_name = book_detail_tree.xpath('//div[@class="book"]/div[@class="info"]/h2/text()')[0]
create_path('./' + book_name)

chapter_dd_list = book_detail_tree.xpath('//div[@class="listmain"]/dl/dd')

def down_chapter(dd):
    chapter_url = 'https://www.bqvvxg8.cc/' + dd.xpath('./a/@href')[0]
    chapter_title = dd.xpath('./a/text()')[0].replace('?', '？')
    chapter_txt_path = './' + book_name +'/' + chapter_title + '.txt'
    if not os.path.exists(chapter_txt_path):
        chapter_content = requests.get(url=chapter_url, headers=headers).text
        chapter_tree = etree.HTML(chapter_content)
        chapter_text = chapter_tree.xpath('//*[@id="content"]/text()')

        # 保存章节
        with open(chapter_txt_path, 'a', encoding='UTF-8') as file:
            file.write(chapter_title)
            for i in range(1, chapter_text.__len__() - 3):
                file.write(chapter_text[i])
        print(chapter_title, " 下载成功")


pool = Pool(20)
pool.map(down_chapter, chapter_dd_list)

pool.close()
pool.join()