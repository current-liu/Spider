# coding=utf-8

import requests
from bs4 import BeautifulSoup
import pymysql
import re
import urlparse
from openpyxl import Workbook

DOWNLOAD_URL = 'http://www.hldptpark.gov.cn/Category_11/Index.aspx'
wb = Workbook()
dest_filename = 'hldptpark.xlsx'
ws1 = wb.active
ws1.title = 'news'


def download_page(url):
    data = requests.get(url).content
    return data


def get_li(doc):
    titles = []
    contents = []
    dates = []
    soup = BeautifulSoup(doc, "html.parser")
    # <div class="left_pic_list">
    div = soup.find("div", class_="left_pic_list")
    ul = div.find("ul")

    for li in ul.find_all("li"):
        title = li.find("div", class_="pe_u_thumb_title").find("a").get_text()
        # br 不是标签 获取不到
        content = li.find("div", class_="pe_u_thumb_title").find("a").next_sibling.next_sibling
        # content = li.find("div", class_="pe_u_thumb_title").find("br").get_text()
        date = li.find("div", class_="datetime").get_text()
        # t = li.find("div", class_="pe_u_thumb_title").get_text()
        # print title, content, date,
        titles.append(title)
        contents.append(content)
        dates.append(date)

    # text=re.compile('下一页') 写成这样就不行
    page = div.find("div", id="page").find('a', text='下一页')
    url = None
    if page:
        url = page['href']
    # print page['href']

    return titles, contents, dates, url


def main():
    titles = []
    contents = []
    dates = []
    url = DOWNLOAD_URL

    # 爬几页
    index = 10

    while url:
        doc = download_page(url)
        title, content, date, new_url = get_li(doc)
        titles += title
        contents += content
        dates += date
        url = urlparse.urljoin(url, new_url)
        index -= 1
        if index:
            pass
        else:
            break

    for (t, c, d) in zip(titles, contents, dates):
        # 这里不能用title，重名的title会使index（）函数返回第一个匹配的值
        index = contents.index(c) + 1
        col_A = 'A%s' % index
        col_B = 'B%s' % index
        col_C = 'C%s' % index

        ws1[col_A] = d
        ws1[col_B] = t
        ws1[col_C] = c
        print index, t, c, d
    wb.save(filename=dest_filename)

    # print get_li(doc)


if __name__ == '__main__':
    main()
