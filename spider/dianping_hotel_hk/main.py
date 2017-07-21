# coding=utf-8
import html_parser
import html_download
import url_manager
import output
import urlparse
import re
from bs4 import BeautifulSoup

def main():
    print "begin"
    GOAL_URL = "http://www.dianping.com/hongkong/hotel/r2827"
    url_manager.add_new_url(GOAL_URL)
    # doc = html_download.downloadPage(GOAL_URL)
    # soup = html_parser.htmlParser(doc)
    # print doc

    ids = []
    names = []
    detail_urls = []
    addrs = []
    walks = []
    tags = []
    prices = []
    stars = []
    review_nums = []

    while (url_manager.has_new_url()):
        url = url_manager.get_new_url()
        print url
        doc = html_download.downloadPage(url)
        shop_id, name, detail_url, addr, walk, tag, price, star, review_num = html_parser.htmlParser(doc)
        # print content
        ids += shop_id
        names += name
        detail_urls += detail_url
        addrs += addr
        walks += walk
        tags += tag
        prices += price
        stars += star
        review_nums += review_num

    for (i, n, d, a, w, t, p, s, r) in zip(ids, names, detail_urls, addrs, walks, tags, prices, stars, review_nums):
        print i, n, d, a, w, t, p, s, r
        tags = " ".join(t)
        output.insert(i, n, d, a, w, tags, p, s, r)


def crawling_shop():
    output.insert_hotel_shops()

    print "crawling_shop()"

    SHOP_URL = "http://www.dianping.com/shop/3715216"
    # shop_id_list = output.downloadShopUrl()
    # for shop_id in shop_id_list:
    #     i = str(shop_id)
    #     s = re.sub(r'\D', "", i)
    #     new_url = urlparse.urljoin(SHOP_URL, s)
    #     url_manager.add_new_shop_url(new_url)

    init_url_list(SHOP_URL)

    shopIds = []
    addrs = []
    tels = []
    openTimes = []
    checkTimes = []
    facss = []
    room_facss = []
    servicess = []
    infos = []
    while (url_manager.has_new_shop_url()):

        url = url_manager.get_new_shop_url()
        shopId = int(re.sub(r'\D', "", url))

        doc = html_download.downloadPage(url)

        addr, tel, openTime, checkTime, facs, room_facs, services, info = html_parser.shopParser(doc)

        shopIds.append(shopId)
        addrs.append(addr)
        tels.append(tel)
        openTimes.append(openTime)
        checkTimes.append(checkTime)
        facss.append(facs)
        room_facss.append(room_facs)
        servicess.append(services)
        infos.append(info)

        print shopId

    # url = url_manager.get_new_shop_url()
    # shopId = int(re.sub(r'\D', "", url))
    # doc = html_download.downloadPage(url)
    # addr, tel, openTime, checkTime, facs, services, info = html_parser.shopParser(doc)
    #
    # shopIds.append(shopId)
    # addrs.append(addr)
    # tels.append(tel)
    # openTimes.append(openTime)
    # checkTimes.append(checkTime)
    # facss.append(facs)
    # servicess.append(services)
    # infos.append(info)
    #
    # print shopId

    for (s, a, t, o, c, f, rf, ss, i) in zip(shopIds, addrs, tels, openTimes, checkTimes, facss, room_facss, servicess,
                                             infos):
        fac = " ".join(f)
        room_facs = " ".join(rf)
        service = " ".join(ss)
        output.update_hotel_shops(s, a, t, o, c, fac, room_facs, service, i)
        pass


# def crawling_room():
#     print "crawling_room()"
#     SHOP_URL = "http://www.dianping.com/shop/3715216"
#     init_url_list(SHOP_URL)
#
#     while (url_manager.has_new_shop_url()):
#         url = url_manager.get_new_shop_url()
#         shopId = int(re.sub(r'\D', "", url))
#         doc = html_download.downloadPage(url)


def init_url_list(goal_url):
    shop_id_list = output.downloadShopUrl()
    for shop_id in shop_id_list:
        i = str(shop_id)
        s = re.sub(r'\D', "", i)
        new_url = urlparse.urljoin(goal_url, s)
        url_manager.add_new_shop_url(new_url)


if __name__ == "__main__":
    # 酒店列表
    # main()

    # 酒店详情
    # crawling_shop()

    url = "http://www.dianping.com/shop/3715216"
    doc = html_download.downloadPage(url)
    soup = BeautifulSoup(doc, "lxml")
    html_parser.crawling_room(soup)
