import random
import time
from urllib import request
from bs4 import BeautifulSoup
import re
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) App' \
                  'leWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
}
content_url = "https://www.rzlib.net/b/21/21258/"  # 小说目录链接
# url = content_url[:re.search(".com", content_url).span()[1]]  # 网站链接


base_url = "https://www.rzlib.net"


def get_link():
    req = request.Request(content_url)
    html = request.urlopen(req).read()
    # print(html)
    result = html.decode("gbk")  # 用某种编码方式解释网页
    soup = BeautifulSoup(result, 'lxml')

    # print(soup)
    dl = soup.find_all('a')

    # print(dl)
    # start_tag = False
    count_num = 1
    # for item in dl:
    #     # print(item)
    #     print("计数：", count_num)
    #     count_num = count_num + 1
    #
    #     # print(item.get('href'))
    #
    #     content_url_1 = item.get('href')
    #     # print(content_url_1)
    #
    #     if  content_url_1 is None:
    #         continue
    #     if content_url_1.endswith(".php"):
    #         continue
    #     if content_url_1.endswith(".net"):
    #         continue
    #
    #     if content_url_1.endswith(".html") and content_url_1.startswith("/b/21/21258"):
    #         # print(item.string + ":" + url + item.a["href"])
    #         # print(content_url_1)
    #
    #         try:
    #
    #             get_content(item.string, base_url + content_url_1)
    #         except:
    #             pass
    #         # break

    # https: // www.rzlib.net / b / 21 / 21258 / 23056939.
    # html
    for num in range(23056939,23056949):

        print(num - 11010347 )
        url = "https://www.rzlib.net/b/21/21258/"+str(num)+".html"
        time.sleep(random.randint(1,10))
        get_content("a",url)

def get_content(title, text_url):
    # print(title)
    print("接收到的ulr",text_url)

    chapter_req = request.Request(text_url)
    html = request.urlopen(chapter_req,timeout=1).read()
    result = html.decode("gbk")
    soup = BeautifulSoup(result, "lxml")
    # print(soup)
    # find_all = soup.find(attrs={"id": "nr_title"})
    #
    div_content = soup.find(attrs={ "id": "chapter_content"})  # 找到小说正文部分的元素

    print(div_content)
    #
    # try:
    #     chapter_title = find_all.get_text()
    #     chapter_content = div_content.get_text()
    # except:
    #     find_all = soup.find(attrs={"id": "chapter_title"})
    #
    #     div_content = soup.find(attrs={ "id": "chapter_content"})  # 找到小说正文部分的元素
    #
    #     chapter_title = find_all.get_text()
    #     chapter_content = div_content.get_text()
    #     print(" 获取标题报错")
    #
    #
    # # 去掉里面没有用的标签
    #
    # if "xiedu" not in os.listdir("./myProject/utllib"):
    #     os.makedirs("./myProject/utllib/xiedu")
    #
    # if '\n' in chapter_title :
    #     chapter_title = chapter_title.replace('\n','')
    #
    # txt_file = open("./myProject/utllib/xiedu/" + chapter_title + ".txt", "w", encoding='utf-8')  # 打开文件，不存在则创建
    #
    # lines = re.sub('[\xa0]+', "\r\n\r\n", chapter_content)  # 将'\xa0'替换为换行符
    # txt_file.writelines(lines)  # 写数据到文件


if __name__ == "__main__":
    get_link()
