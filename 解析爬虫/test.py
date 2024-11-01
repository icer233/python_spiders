# import unicodedata

# def get_display_width(text):
#     width = 0
#     for char in text:
#         if unicodedata.east_asian_width(char) in 'WF':
#             width += 2
#         else:
#             width += 1
#     return width

# def format_text(text, width):
#     display_width = get_display_width(text)
#     padding = width - display_width
#     return text + ' ' * padding
# name1 = '上海市第十五届高二物理竞赛复赛试题（附解答）'
# name2 = '上海市第五届高二物理竞赛试题（附答案）'
# name3 = '上海市第十六届高二物理竞赛（浦东新区洋泾中学杯）初赛试题（附答案）'
# name = '11'
# width = 85

# # print(f"{format_text(name, width)}\t\033[0;34m\033[1m已存在！\033[0m")
# # print(f"{format_text(name, width)}\t\033[0;37m\033[1m开始下载......\033[0m")
# # print(f"{format_text(name, width)}\t\033[1m下载成功！\033[0m")

# txtt = '\033[0;37m\033[1m文件\033[0m'
# print(f"{format_text(txtt, width)}\t\033[0;34m\033[1m状态\033[0m")
import re
detail_text = 'http://files.eduu.com/down.php?id=288283'
down_url = re.findall('(http://files\.eduuu\.com/ohr/.*?\.rar)|(http://files\.eduu\.com/down\.php\?id=288283)', detail_text, re.S)[0]
if down_url[0]:
    print(down_url[0])
else:
    print(down_url[1])