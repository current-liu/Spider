# coding=utf-8
import h_parser
import html_download
import url_manager
import dao
import urlparse
import re
from bs4 import BeautifulSoup
import datetime
import result_manager
import time
import random
import traceback


def crawling_hotel_list():
    print "begin crawling_hotel_list()"
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
    picUrls = []
    while (url_manager.has_new_url()):
        time.sleep(random.uniform(0.5, 1))
        url = url_manager.get_new_url()
        print url
        doc = html_download.downloadPage(url)
        shop_id, name, detail_url, addr, walk, tag, price, star, review_num, picUrl = h_parser.htmlParser(doc)
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
        picUrls += picUrl
    for (i, n, d, a, w, t, p, s, r, pu) in zip(ids, names, detail_urls, addrs, walks, tags, prices, stars, review_nums,
                                               picUrls):
        print i, n, d, a, w, t, p, s, r, pu
        tags = " ".join(t)

        # 修改
        dao.insert(i, n, d, a, w, tags, p, s, r, pu)


def crawling_shop():
    dao.insert_hotel_shops()

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

        addr, tel, openTime, checkTime, facs, room_facs, services, info = h_parser.shopParser(doc)

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
        dao.update_hotel_shops(s, a, t, o, c, fac, room_facs, service, i)
        pass


def crawling_room():
    print "crawling_room()"
    index = 0
    ROOM_URL = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=3715216&" \
               "checkinDate=2017-08-01&checkoutDate=2017-08-02"
    init_room_url_list(ROOM_URL)

    # shopIds_total = []
    # roomIds_total = []
    # titles_total = []
    # bedTypes_total = []
    # breakfasts_total = []
    # netTypes_total = []
    # cancelRules_total = []
    # prices_total = []
    index = 0
    while (url_manager.has_new_room_url()):

        time.sleep(random.uniform(2, 3))

        urls = url_manager.get_new_room_url()
        index += 1
        s = urls.split("checkinDate")[0]
        shopId = int(re.sub(r'\D', "", s))
        print "crawling 第'%s'个：'%s'" % (index, shopId)
        url_list = urls.split(" ")

        doc0 = html_download.downloadPage(url_list[0])
        doc1 = html_download.downloadPage(url_list[1])
        doc2 = html_download.downloadPage(url_list[2])
        doc3 = html_download.downloadPage(url_list[3])
        doc4 = html_download.downloadPage(url_list[4])
        doc_list = (doc0, doc1, doc2, doc3, doc4)

        rooms_info_total = h_parser.get_room(doc_list, shopId)

        today = datetime.date.today()
        query_time = today.strftime("%Y-%m-%d")

        if rooms_info_total == None:
            room_info_list = [{"roomInfo": [-1, shopId, "此shopId未查询到数据", -1, -1, -1, -1, -1]}]
            dao.insert_hotel_rooms(room_info_list, query_time)
            print "无信息", shopId
            continue

        room_info_list = []
        for room_infos in rooms_info_total:
            if room_infos[1] == 0:
                room_info_list = room_infos[0]
                pass
            else:
                for room in room_infos[0]:
                    for r in room_info_list:
                        if r["roomId"] == room["roomId"]:
                            r["roomInfo"].append(room["roomInfo"][3])
        print "扒完", shopId

        dao.insert_hotel_rooms(room_info_list, query_time)




        # shopIds_total += shopIds
        # roomIds_total += roomIds
        # titles_total += titles
        # bedTypes_total += bedTypes
        # breakfasts_total += breakfasts
        # netTypes_total += netTypes
        # cancelRules_total += cancelRules
        # prices_total += prices

        # print "爬取完毕，开始插入数据"
        # dao.insert_hotel_goods(shopIds_total, roomIds_total, titles_total, bedTypes_total, breakfasts_total,
        #                        netTypes_total, cancelRules_total, prices_total)


def crawling_review():
    print "crawling_shop()"

    # 从数据库中读取已爬过的review_url
    # init_old_review_urls()

    # 初始化new_review_urls
    init_review_url_list()

    # 打印All new_review
    url_manager.print_new_review_url()
    print "hhh"

    # REVIEW_URL = "/3715216/review_more"
    # url_manager.new_review_urls = set()
    # url_manager.add_new_review_url(REVIEW_URL)

    try:
        while (url_manager.has_new_review_url()):

            time.sleep(random.uniform(2, 5))

            identify_url = url_manager.get_new_review_url()
            if identify_url:
                url = "http://www.dianping.com/shop" + identify_url

                print url
            else:
                print identify_url
                raise BaseException

            doc = html_download.downloadPage(url)
            if doc == "error":
                url_manager.add_new_review_url(identify_url)
                print "download error"
                continue
            elif doc == "403":
                url_manager.add_new_review_url(identify_url)
                print "403"

                continue
            else:
                result = h_parser.get_review(doc, url)

            if result:
                result_manager.add_new_result(result)
                dao.insert_hotel_review()
    except BaseException, e:
        print e
        print traceback.format_exc()


# def init_old_review_urls():
#     """#从数据库中读取已爬过的review_url"""
#     message = raw_input("是否从数据库中读取new_review_url？y/n")
#     if message == 'y':
#         dao.init_old_review_urls()
#         print "将从数据库中读取new_review_url"
#         u = url_manager.old_review_urls
#         print u
#     elif message == 'n':
#         print "您选择了No"
#     else:
#         print "输入有误"
#         init_old_review_urls()


def init_shop_url_list(goal_url):
    shop_id_list = dao.downloadShopUrl()
    for shop_id in shop_id_list:
        i = str(shop_id)
        s = re.sub(r'\D', "", i)
        new_url = urlparse.urljoin(goal_url, s)
        url_manager.add_new_shop_url(new_url)


def init_room_url_list(goal_url):
    today = datetime.date.today()
    after_1 = today + datetime.timedelta(days=1)
    after_2 = today + datetime.timedelta(days=2)
    after_3 = today + datetime.timedelta(days=3)
    after_4 = today + datetime.timedelta(days=4)
    after_5 = today + datetime.timedelta(days=5)

    checkinDate_0 = today.strftime("%Y-%m-%d")
    checkoutDate_0 = after_1.strftime("%Y-%m-%d")
    checkinDate_1 = after_1.strftime("%Y-%m-%d")
    checkoutDate_1 = after_2.strftime("%Y-%m-%d")
    checkinDate_2 = after_2.strftime("%Y-%m-%d")
    checkoutDate_2 = after_3.strftime("%Y-%m-%d")
    checkinDate_3 = after_3.strftime("%Y-%m-%d")
    checkoutDate_3 = after_4.strftime("%Y-%m-%d")
    checkinDate_4 = after_4.strftime("%Y-%m-%d")
    checkoutDate_4 = after_5.strftime("%Y-%m-%d")
    shop_id_list = dao.downloadShopUrl()

    for shop_id in shop_id_list:
        i = str(shop_id)
        s = re.sub(r'\D', "", i)
        str1 = "hotelPrepayAndOtaGoodsList?shopId="
        str2 = "&checkinDate="
        str3 = "&checkoutDate="

        # 'http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=3715216&checkinDate=2017-07-24&checkoutDate=2017-07-25'
        s0 = str1 + s + str2 + checkinDate_0 + str3 + checkoutDate_0
        s1 = str1 + s + str2 + checkinDate_1 + str3 + checkoutDate_1
        s2 = str1 + s + str2 + checkinDate_2 + str3 + checkoutDate_2
        s3 = str1 + s + str2 + checkinDate_3 + str3 + checkoutDate_3
        s4 = str1 + s + str2 + checkinDate_4 + str3 + checkoutDate_4
        new_url_0 = urlparse.urljoin(goal_url, s0)
        new_url_1 = urlparse.urljoin(goal_url, s1)
        new_url_2 = urlparse.urljoin(goal_url, s2)
        new_url_3 = urlparse.urljoin(goal_url, s3)
        new_url_4 = urlparse.urljoin(goal_url, s4)
        url_manager.add_new_room_url(new_url_0 + " " + new_url_1 + " " + new_url_2 + " " + new_url_3 + " " + new_url_4)
    u = url_manager.new_room_urls
    pass


def init_review_url_list():
    message = raw_input("是否根据shopId初始化new_review_urls？选择否将根据数据库new_review_url初始化?:y/n")
    if message == 'y':
        print "您选择了Yes"
        shop_id_list = dao.downloadShopUrl()
        for shop_id in shop_id_list:
            i = str(shop_id)
            s = re.sub(r'\D', "", i)
            new_url = "/" + s + "/review_more"
            url_manager.add_new_review_url(new_url)
    elif message == 'n':
        print "您选择了No，将根据数据库中的表hotel_new_review_url初始化new_review_urls"
        r = dao.select_new_review_urls()
        l = list(r)
        # if r:
        #     for url in r:
        #         x = url[0]
        #         l.append(str(x))
        #
        try:
            url_manager.add_new_review_urls(l)
        except BaseException, e:
            print "根据数据库中的表hotel_new_review_url初始化new_review_urls，失败"
        else:
            print "根据数据库中的表hotel_new_review_url初始化new_review_urls，done"

    else:
        print "输入有误"
        init_review_url_list()


if __name__ == "__main__":
    # 酒店列表
    # crawling_hotel_list()

    # 酒店详情
    # crawling_shop()


    # 房间详情
    crawling_room()

    # try:
    #     crawling_review()
    # except BaseException, e:
    #     url_manager.insert_new_review_url_into_db()

    # url = "http://www.dianping.com/shop/3715216/review_more"
    # doc = html_download.downloadPage(url)
    # result = h_parser.get_review(doc, 3715216)
    # result_manager.add_new_result(result)
    # output.insert_hotel_review()
    # # print doc
    # url = "http://www.baidu.com"
    # html_download.downloadPage(url)
    pass
