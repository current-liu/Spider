# coding=utf-8
import html_parser
import html_download
import url_manager
import output
import urlparse
import re
from bs4 import BeautifulSoup
import datetime


def hotel_list():
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

    init_shop_url_list(SHOP_URL)

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


def crawling_room():
    print "crawling_room()"
    index = 0
    ROOM_URL = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=3715216&" \
               "checkinDate=2017-07-24&checkoutDate=2017-07-25"
    init_room_url_list(ROOM_URL)

    shopIds_total = []
    roomIds_total = []
    titles_total = []
    bedTypes_total = []
    breakfasts_total = []
    netTypes_total = []
    cancelRules_total = []
    prices_total = []

    while (url_manager.has_new_room_url()):
        index += 1
        print index

        url = url_manager.get_new_room_url()
        s = url.split("checkinDate")[0]
        shopId = int(re.sub(r'\D', "", s))

        doc = html_download.downloadPage(url)
        shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices = html_parser.get_room(doc,
                                                                                                             shopId)

        shopIds_total += shopIds
        roomIds_total += roomIds
        titles_total += titles
        bedTypes_total += bedTypes
        breakfasts_total += breakfasts
        netTypes_total += netTypes
        cancelRules_total += cancelRules
        prices_total += prices

    print "爬取完毕，开始插入数据"
    output.insert_hotel_goods(shopIds_total, roomIds_total, titles_total, bedTypes_total, breakfasts_total,
                              netTypes_total, cancelRules_total, prices_total)


def crawling_review():
    print "crawling_shop()"
    REVIEW_URL = "http://www.dianping.com/shop/3715216/review_more"
    init_review_url_list(REVIEW_URL)

    while (url_manager.has_new_review_url()):
        shopId = int(re.sub(r'\D', "", url))
        url = url_manager.get_new_review_url()
        doc = html_download.downloadPage(url)


def init_shop_url_list(goal_url):
    shop_id_list = output.downloadShopUrl()
    for shop_id in shop_id_list:
        i = str(shop_id)
        s = re.sub(r'\D', "", i)
        new_url = urlparse.urljoin(goal_url, s)
        url_manager.add_new_shop_url(new_url)


def init_room_url_list(goal_url):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    checkinDate = today.strftime("%Y-%m-%d")
    checkoutDate = tomorrow.strftime("%Y-%m-%d")
    shop_id_list = output.downloadShopUrl()

    for shop_id in shop_id_list:
        i = str(shop_id)
        s = re.sub(r'\D', "", i)
        str1 = "hotelPrepayAndOtaGoodsList?shopId="
        str2 = "&checkinDate="
        str3 = "&checkoutDate="

        # 'http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=3715216&checkinDate=2017-07-24&checkoutDate=2017-07-25'
        s = str1 + s + str2 + checkinDate + str3 + checkoutDate
        new_url = urlparse.urljoin(goal_url, s)
        url_manager.add_new_room_url(new_url)


def init_review_url_list(goal_url):
    shop_id_list = output.downloadShopUrl()
    for shop_id in shop_id_list:
        i = str(shop_id)
        s = re.sub(r'\D', "", i)
        new_url = urlparse.urljoin(goal_url, s)
        url_manager.add_new_review_url(new_url)


if __name__ == "__main__":
    # 酒店列表
    # hotel_list()

    # 酒店详情
    # crawling_shop()


    # 房间详情
    # crawling_room()


    # crawling_review()
    doc = html_download.downloadPage("http://www.dianping.com/shop/3715216/review_more")
    soup = html_parser.get_review(doc,3715216)
    print doc
    pass
