import urllib.request
from lxml import etree
import json
 
# [url]https://www.sanguosha.com/msgs/mWallPaper[/url]
# [url]https://www.sanguosha.com/msgs/mWallPaper/cur/2[/url]
# [url]https://www.sanguosha.com/msgs/mWallPaper/cur/3[/url]
 
 
def get_content(page):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"}
    if page == 1:
        first_url = "https://www.sanguosha.com/msgs/mWallPaper"
        request_first = urllib.request.Request(url=first_url, headers=headers)
        response = urllib.request.urlopen(request_first)
        content_first = response.read().decode("utf-8")
        num = 0
        tree = etree.HTML(content_first)
        https_list = tree.xpath("/html/body/div[1]/div/div//@href")
        for i in range(len(https_list)):
            url = https_list[i]
            num += 1
            urllib.request.urlretrieve(url=url, filename="D:/三国杀十周年壁纸/" + "00" + str(num) + ".jpg")
    else:
        url = "https://www.sanguosha.com/msgs/mWallPaper/cur/" + str(page)
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode("utf-8")
        with open("三国杀十周年壁纸爬虫.json", "w", encoding="utf-8") as file:
            file.write(content)
 
 
def json_data():
    json_file = json.load(open("三国杀十周年壁纸爬虫.json", "r", encoding="utf-8"))
    for i in range(len(json_file)):
        https_data = json_file[i]["imgurl"]
        name = json_file[i]["title"].replace("*", "-")
        urllib.request.urlretrieve(url=https_data, filename="D:/三国杀十周年壁纸/" + name + ".jpg")
 
 
if __name__ == '__main__':
    begin_page = int(input("请输入起始页码："))
    end_page = int(input("请输入起始结束："))
    for page in range(begin_page, end_page + 1):
        get_content(page)
        json_data()