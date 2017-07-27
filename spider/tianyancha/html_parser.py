# coding=utf-8

from bs4 import BeautifulSoup
import re
import url_manager


def htmlParser(doc):
    soup = BeautifulSoup(doc, "lxml")
    ul = soup.find("div", class_="b-c-white search_result_container")

    pic_urls = []
    emoji_names = []
    create_times = []
    contents = []
    labels = []
    replys = []

    for li in ul.find_all("div",recursive=False):
        # print li.get_text()
        # print "------------------------------------------"

        content = li.find("div", class_="col-xs-10 search_repadding2 f18").find("a")['href']

        label = li.find("div", class_="topic_label").get_text()
        reply = li.find("div", class_="k11_reply_con").get_text()
        # print pic_url, emoji_name, create_time, content, label, reply
        # print "------------------------------------------"
        pic_urls.append(pic_url.strip())
        emoji_names.append(emoji_name.strip())
        create_times.append(create_time.strip())
        contents.append(content.strip())
        labels.append(label.strip())
        replys.append(reply.strip())
    """获取下一页的url"""
    # onclick = "window.location.href=&quot;http://www.shanghaik11.com/index.php?m=content&amp;c=index&amp;a=lists&amp;catid=90&amp;page=4&amp;orderby=&quot;" > 下一页 & gt; < / span >
    page_box = soup.find("div", class_="page_box_iris")
    last_page = page_box.find('span', text='末页')
    next_page = last_page.previous_sibling.previous_sibling
    # print "next_page", next_page
    # next_url = None
    # 'window.location.href="http://www.shanghaik11.com/index.php?m=content&c=index&a=lists&catid=90&page=2&orderby="'

    http_url = next_page["onclick"]
    # reg = re.compile('".*"')
    # http_url = re.search(reg, next_url)
    string = str(http_url)
    next_url = string.split('"')[1]
    # print next_url
    url_manager.add_new_url(next_url)
    # str_last = str(last_page["onclick"]).split("orderby")[0]
    # str_next = str(next_page["onclick"]).split("orderby")[0]

    return pic_urls, emoji_names, create_times, contents, labels, replys
