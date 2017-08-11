# coding=utf-8
import os

import h_parser
import html_download
import url_manager
import dao
import urlparse
import re
import datetime
import result_manager
import time
import random
import traceback

today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")
today_fo = today.strftime("%Y%m%d")
os.chdir("."+"/log")
filename = today_fo+".txt"
fo_log = open(filename, "a")


def crawling_hotel_list():
    print "begin crawling_hotel_list()"
    # GOAL_URL = "http://www.dianping.com/hongkong/hotel/r2827"
    # 新解
    GOAL_URL1 = "http://www.dianping.com/hongkong/hotel/r2844"
    # 离岛
    GOAL_URL2 = "http://www.dianping.com/hongkong/hotel/r2857"
    # 九龙
    GOAL_URL3 = "http://www.dianping.com/hongkong/hotel/r2826"
    # 香港岛
    GOAL_URL4 = "http://www.dianping.com/hongkong/hotel/r2807"

    url_manager.add_new_url(GOAL_URL3)
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
        doc, msg = html_download.downloadPage(url)
        if msg != "ok":
            continue

        shop_id, name, detail_url, addr, walk, tag, price, star, review_num, picUrl = h_parser.get_hotel_list(doc)
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
        dao.insert_hotel_list(i, n, d, a, w, tags, p, s, r, pu)


def crawling_shop():
    # 有新的酒店时，需执行此
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

    # shopIds = []
    # addrs = []
    # tels = []
    # openTimes = []
    # checkTimes = []
    # facss = []
    # room_facss = []
    # servicess = []
    # infos = []
    # review_nums = []

    index = 1
    while (url_manager.has_new_shop_url()):
        url = url_manager.get_new_shop_url()
        # url = 'http://www.dianping.com/shop/4567229'
        shopId = int(re.sub(r'\D', "", url))

        print "下载并解析第%s个shopId:" % index, shopId
        index += 1

        doc, msg = html_download.downloadPage(url)
        if msg == "ok":
            addr, tel, openTime, checkTime, facs, room_facs, services, info, review_num = h_parser.hotel_shop_parser(
                doc)
        else:
            print "下载酒店详情页失败"

        facs_ = " ".join(facs)
        room_facs_ = " ".join(room_facs)
        services_ = " ".join(services)
        dao.update_hotel_shops(shopId, addr, tel, openTime, checkTime, facs_, room_facs_, services_, info, review_num)

        # shopIds.append(shopId)
        # addrs.append(addr)
        # tels.append(tel)
        # openTimes.append(openTime)
        # checkTimes.append(checkTime)
        # facss.append(facs)
        # room_facss.append(room_facs)
        # servicess.append(services)
        # infos.append(info)
        # review_nums.append(review_num)

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

        # print "正在写入数据库，请稍后"
        # #  应该修改为每查询一个酒店的信息就插入，避免中间错误导致数据丢失
        # for (s, a, t, o, c, f, rf, ss, i, n) in zip(shopIds, addrs, tels, openTimes, checkTimes, facss, room_facss,
        #                                             servicess,
        #                                             infos, review_nums):
        #     fac = " ".join(f)
        #     room_facs = " ".join(rf)
        #     service = " ".join(ss)
        #     dao.update_hotel_shops(s, a, t, o, c, fac, room_facs, service, i, n)
        #     pass


def crawling_room():
    print "crawling_room()"

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

        time.sleep(random.uniform(1, 2))

        urls = url_manager.get_new_room_url()
        index += 1
        s = urls.split("checkinDate")[0]
        shopId = int(re.sub(r'\D', "", s))
        print "crawling_room 第'%s'个shopId：'%s'" % (index, shopId)
        url_list = urls.split(" ")

        doc0, msg = html_download.downloadPage_without_proxy(url_list[0])
        doc1, msg = html_download.downloadPage_without_proxy(url_list[1])
        doc2, msg = html_download.downloadPage_without_proxy(url_list[2])
        doc3, msg = html_download.downloadPage_without_proxy(url_list[3])
        doc4, msg = html_download.downloadPage_without_proxy(url_list[4])
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


def get_attraction_review_on_page(shopId, page_num):
    flag = True
    index = 1
    while (flag):
        if index == page_num:
            flag = False

        review_url = "http://www.dianping.com/shop/" + str(shopId) + "/review_all_latest?pageno=" + str(index)

        msg14 = "小循环循环到(total '%d'):" % page_num
        print msg14
        print review_url
        fo_log.write(msg14 + review_url)
        # TODO对html_download.downloadPage(url)返回的结果应该进行处理，判断msg，所有地方用到此函数的都要处理
        doc, msg = html_download.downloadPage(review_url)
        if msg != "ok":
            continue

        try:
            result = h_parser.get_attraction_review(shopId, doc, review_url)
            timeout = result[-1]
            if timeout:
                flag = False
                print "截止2010年，更早的舍弃"
        except BaseException, e:
            # TODO应该把doc打印出来,有问题但在html_download里面未被拦截的doc
            print e
            # TODO打成单独文件
            filename1 = "'%s'doc_with_error.txt" % today_fo
            fo_log_doc_with_error = open(filename1, "a")
            fo_log_doc_with_error.write("doc with error:'%d'" % shopId)
            fo_log_doc_with_error.write(doc)

        res = ""
        if result:
            result_manager.add_new_attraction_review_result(result)
            res = dao.insert_attraction_review()

        if res == "for key 'PRIMARY'":
            msg16 = "shopId %s 已循环到已经爬过内容" % shopId
            print msg16
            fo_log.write(msg16)
            break

        else:
            index += 1

    msg17 = "shopId %s log to pageno=%s" % (shopId, index)
    print msg17
    fo_log.write(msg17)


def crawling_attraction_review():
    """评论总数从attraction_sops表中直接读取，同shopId一起传过来"""
    print "crawling_attraction_review()"
    try:
        res = dao.select_shopid_and_reviewnum("attraction_shops")
    except BaseException, e:
        print e
    for shop in res:
        try:
            index = res.index(shop) + 1
            shopId = shop[0]
            review_num = shop[1]
            if review_num < 1:
                continue
            elif review_num % 20 == 0:
                page_num = review_num / 20
            else:
                page_num = 1 + review_num / 20
        except BaseException:
            msg11 = "解析shopId，page_num失败"
            print msg11

        msg12 = "大循环循环到第'%s'：'%s'" % (index, shopId)
        print msg12
        fo_log.write(msg12)

        # 爬取页面上的评论
        get_attraction_review_on_page(shopId, page_num)


def crawling_hotel_review_02():
    """评论总数从hotel_sops表中直接读取，同shopId一起传过来"""
    print "crawling_review()"
    try:
        res = dao.select_shopid_and_reviewnum("hotel_shops")
    except BaseException, e:
        print e
    for shop in res:
        try:
            index = res.index(shop) + 1
            shopId = shop[0]
            review_num = shop[1]
            if review_num < 1:
                continue
            elif review_num % 20 == 0:
                page_num = review_num / 20
            else:
                page_num = 1 + review_num / 20
        except BaseException:
            msg1 = "解析shopId，page_num失败"
            print msg1

        msg1 = "大循环循环到第'%s'：'%s'" % (index, shopId)
        print msg1
        fo_log.write(msg1)

        # 爬取页面上的评论
        get_hotel_review_on_page(shopId, page_num)


def get_hotel_review_on_page(shopId, page_num):
    flag = True
    while (flag):
        if page_num == 1:
            flag = False

        review_url = "http://www.dianping.com/shop/" + str(shopId) + "/review_more_newest?pageno=" + str(page_num)
        msg4 = "小循环循环到:"
        print msg4
        print review_url
        fo_log.write(msg4 + review_url)
        # TODO对html_download.downloadPage(url)返回的结果应该进行处理，判断msg，所有地方用到此函数的都要处理
        doc, msg = html_download.downloadPage(review_url)
        if msg != "ok":
            continue

        try:
            result = h_parser.get_hotel_review(doc, review_url)
        except BaseException, e:
            # TODO应该把doc打印出来,有问题但在html_download里面未被拦截的doc
            print e
            fo_log.write("doc with error")
            fo_log.write(doc)

        res = ""
        if result:
            result_manager.add_new_hotel_review_result(result)
            res = dao.insert_hotel_review()

        if res == "for key 'PRIMARY'":
            msg6 = "shopId %s 已循环到已经爬过内容" % shopId
            print msg6
            fo_log.write(msg6)
            break

        else:
            page_num -= 1

    msg7 = "shopId %s log to pageno=%s" % (shopId, page_num)
    print msg7
    fo_log.write(msg7)


def crawling_hotel_review():
    print "crawling_review()"

    # 从数据库中读取已爬过的review_url
    # init_old_review_urls()

    # 打印All new_review
    # url_manager.print_new_review_url()

    # u_rasie = url_manager.new_review_urls
    # raise BaseException



    # 初始化new_review_urls
    try:
        init_review_url_list()
    except BaseException, e:
        print e
    # REVIEW_URL = "/4567549/review_more"
    # url_manager.add_new_review_url(REVIEW_URL)

    try:
        index_while01 = 0
        # 功能迁移，变量作废
        # get_page_num_record = {}
        while (url_manager.has_new_review_url()):
            index_while01 += 1
            # time.sleep(random.uniform(2, 5))
            # 获取每个shopId的评论首页
            # identify_url:/3715216/review_more
            identify_url = url_manager.get_new_review_url()
            shopId = int(re.sub(r'\D', "", identify_url))
            if identify_url:
                url = "http://www.dianping.com/shop" + identify_url
                msg1 = "大循环循环到第'%s'：'%s'" % (index_while01, shopId)
                print msg1
                print url
                fo_log.write(msg1)
                fo_log.write(url)
            else:
                msg2 = "错误的identify_url:%s" % identify_url
                print msg2
                fo_log.write(msg2)
                raise BaseException

            # 获取每个shopId的评论总页数

            try:
                # TODO异常的处理 html_download.downloadPage(url) 返回的msg
                doc, msg = html_download.downloadPage(url)
                if msg == "ok":
                    totalpage_num = h_parser.get_review_page_num(doc, url)
                else:
                    raise BaseException
            except BaseException, e:
                print e
                msg3 = "获取评论总页数totalpage_num失败" + url
                print msg3
                fo_log.write(msg3)

                # if get_page_num_record.__contains__(url):
                #     if get_page_num_record[url] < 3:
                #         get_page_num_record[url] = get_page_num_record[url] + 1
                #         url_manager.remove_old_review_urls(identify_url)
                #         url_manager.add_new_review_url(identify_url)
                #         continue
                #     else:
                #         # 放弃获取该ID的totalpage_num
                #         msg3 = "放弃获取该ID的totalpage_num：" + url
                #         print msg3
                #         continue
                # else:
                #     get_page_num_record[url] = 1
                #     url_manager.remove_old_review_urls(identify_url)
                #     url_manager.add_new_review_url(identify_url)
                #     continue

            # 按评论总页数，从最后一页开始往前爬
            page_num = totalpage_num

            # 功能迁移，变量作废
            # down_record = {}

            # TODOwhile(flag) if page_num = 1: flag = False
            flag = True
            while (flag):
                if page_num == 1:
                    flag = False
                else:
                    page_num -= 1

                review_url = "http://www.dianping.com/shop/" + str(shopId) + "/review_more_newest?pageno=" + str(
                    page_num)
                msg4 = "小循环循环到:"
                print msg4
                print review_url
                fo_log.write(msg4 + review_url)
                # TODO对html_download.downloadPage(url)返回的结果应该进行处理，判断msg，所有地方用到此函数的都要处理
                doc, msg = html_download.downloadPage(review_url)
                if msg != "ok":
                    continue
                # 这块功能迁移到html_download.py 模块中，更为合理
                # if msg != "ok":
                #     if down_record.__contains__(page_num):
                #
                #         # 尝试3次，还不行就放弃
                #         if down_record[page_num] < 3:
                #             down_record[page_num] = down_record[page_num] + 1
                #             continue
                #         else:
                #             # 放弃该页面
                #             msg5 = "放弃："+identify_url
                #             print msg5
                #             fo_log.write(msg5)
                #             page_num -= 1
                #             fo = open(
                #                 r"D:\Liuchao\PycharmProjects\pythonproject\spider\dianping_hotel_hk\download_error\'%s''%s'.txt" % (
                #                     today_str, identify_url), "wb")
                #             fo.write(doc)
                #             fo.close()
                #             continue
                #     else:
                #         down_record[page_num] = 1
                #         continue
                #
                # else:
                try:
                    result = h_parser.get_hotel_review(doc, review_url)
                except BaseException, e:
                    print e

                res = ""
                if result:
                    result_manager.add_new_hotel_review_result(result)
                    res = dao.insert_hotel_review()

                if res == "for key 'PRIMARY'":
                    msg6 = "shopId %s 已循环到已经爬过内容" % shopId
                    print msg6
                    fo_log.write(msg6)
                    break

            msg7 = "shopId %s log to pageno=%s" % (shopId, page_num)
            print msg7
            fo_log.write(msg7)

            # 之前的，每次获取下一页连接的处理逻辑
            # doc, msg = html_download.downloadPage(url)
            # if msg != "ok":
            #     url_manager.remove_old_review_urls(identify_url)
            #     url_manager.add_new_review_url(identify_url)
            #     u_test = url_manager.new_review_urls
            #     fo = open(
            #         r"D:\Liuchao\PycharmProjects\pythonproject\spider\dianping_hotel_hk\download_error\'%s''%s'.txt" % (
            #             today_str, identify_url), "wb")
            #     fo.write(doc)
            #     fo.close()
            #     continue
            # else:
            #     result = h_parser.get_review(doc, url)
            #
            # if result:
            #     result_manager.add_new_result(result)
            #     dao.insert_hotel_review()
    except BaseException, be:
        print be
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
    """初始化要查询的酒店，当需要更新全部酒店的信息时，shop_id_list = dao.downloadShopUrl()"""
    # 从hotel_shop_list表中查全部shopId
    # shop_id_list = dao.downloadShopUrl()
    # 查询hotel_shops表中还没有更新酒店详情的shopId
    shop_id_list = dao.downloadShopIdFrom_hotel_shops()

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

    shop_id_list = dao.download_hotel_shopIds_unselected(today_str)

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
    shop_id_list = dao.download_hotel_shopIds()
    for shop_id in shop_id_list:
        i = str(shop_id)
        s = re.sub(r'\D', "", i)
        new_url = "/" + s + "/review_more"
        url_manager.add_new_review_url(new_url)


# 按照评论总页数循环的思路，该方法做出调整
# def init_review_url_list():
#     message = raw_input("是否根据shopId初始化new_review_urls？选择否将根据数据库new_review_url初始化?:y/n")
#     if message == 'y':
#         print "您选择了Yes"
#         shop_id_list = dao.downloadShopUrl()
#         for shop_id in shop_id_list:
#             i = str(shop_id)
#             s = re.sub(r'\D', "", i)
#             new_url = "/" + s + "/review_more"
#             url_manager.add_new_review_url(new_url)
#     elif message == 'n':
#         print "您选择了No，将根据数据库中的表hotel_new_review_url初始化new_review_urls"
#         r = dao.select_new_review_urls()
#
#         # 初始化完成后清空原表
#         dao.truncate_new_review_urls()
#         l = list(r)
#         # if r:
#         #     for url in r:
#         #         x = url[0]
#         #         l.append(str(x))
#         #
#         if l == None:
#             print "表hotel_new_review_url为空，初始化失败!"
#             return
#         try:
#             url_manager.add_new_review_urls(l)
#
#         except BaseException, e:
#             print "根据数据库中的表hotel_new_review_url初始化new_review_urls，失败"
#         else:
#             print "根据数据库中的表hotel_new_review_url初始化new_review_urls，done"
#
#     else:
#         print "输入有误"
#         init_review_url_list()

def crawling_attraction_shop():
    # 需要更新景点名录时调用此函数
    # init_attraction_shop_list()
    try:
        shopIds = dao.download_attraction_shopIds()
    except BaseException, e:
        print e
        msg1 = "shopIds 获取失败"
        print msg1
    for shop in shopIds:
        time.sleep(random.uniform(1, 2))
        shop_id = shop[0]
        id_str = str(shop_id)
        tel = -10
        print "num.%s shopId：%s" % (shopIds.index(shop), shop_id)

        url = "http://www.dianping.com/shop/" + id_str
        doc, msg = html_download.downloadPage_without_proxy(url)
        if msg != "ok":
            continue
        else:
            try:
                shop_name, dict_brief, address, tel, dict_indent = h_parser.attraction_shop_parser(doc)
            except BaseException, e:
                print e
                # print doc
        try:
            dao.update_attraction_shops(shop_id, shop_name, dict_brief, address, tel, dict_indent)
        except BaseException, e:
            print e

    pass


def init_attraction_shop_list():
    """初始化景点列表"""
    attraction_url = "http://www.dianping.com/hongkong/attraction"
    doc, msg = html_download.downloadPage(attraction_url)
    if msg != "ok":
        pass
    else:
        attraction_num = h_parser.get_attraction_num(doc)
        attraction_page_num = 1 + attraction_num / 15
        get_attraction_list(attraction_page_num)


def get_attraction_list(page_num):
    pre_url = "http://www.dianping.com/hongkong/attraction?district=&category=&pageNum="
    flag = True
    index = 0
    while (flag):
        index += 1
        if index == page_num:
            flag = False

        url = pre_url + str(index)
        doc, msg = html_download.downloadPage(url)
        if msg != "ok":
            pass
        else:
            try:
                shopIds, picUrls, tips = h_parser.get_attraction_list(doc)
                dao.insert_attraction_shops(shopIds, tips, picUrls)
            except BaseException, e:
                print e
                print "in get_attraction_list(page_num)"


if __name__ == "__main__":
    # 酒店列表
    # crawling_hotel_list()

    # 酒店详情
    # crawling_shop()

    # 房间详情
    crawling_room()

    # 酒店评论
    # try:
    #    crawling_hotel_review_02()
    #
    # except BaseException, e:
    #     print e
    #     print "程序中止"

    # 景点列表
    # crawling_attraction_shop()

    # 景点评论
    # crawling_attraction_review()
