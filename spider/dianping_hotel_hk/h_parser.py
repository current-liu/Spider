# coding=utf-8

import datetime
import re
import json
import traceback
import urlparse
from bs4 import BeautifulSoup

import url_manager
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


shopId_num = 0
today = datetime.date.today()
today_str = today.strftime("%Y-%m-%d")


def get_hotel_list(doc):
    URL_FULL = "http://www.dianping.com/shop/3715216"
    PAGE_URL = "http://www.dianping.com/hongkong/hotel/r2827"
    soup = BeautifulSoup(doc, "lxml")
    hotel_list = soup.find("ul", class_="hotelshop-list")

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

    for li in hotel_list.find_all("li", class_=" hotel-block J_hotel-block"):
        # print li.get_text()
        # print "------------------------------------------"
        # < a class ="hotel-name-link" data-midas-extends="module=5_hotellist_shop"
        # href = "/shop/3715216"
        # onclick = "_hip.push(['mv',{module:'5_hotellist_shop', action: 'click',content:'/shop/3715216',title:'香港丽思卡尔顿酒店'}]);"
        # target = "_blank"
        # title = "香港丽思卡尔顿酒店" > 香港丽思卡尔顿酒店 < / a >
        # < a class ="ibook" href="/shop/3715216" target="_blank" > < / a >
        try:
            pics = li.find("ul", class_="J_hotel-pics").find("li")
            picUrl = str(pics.find("a"))
        except BaseException, e:
            picUrl = "none"
        # reg = re.compile('http://[\S]*"')
        # imgList = re.search(reg, picUrl)
        # pppp = picUrl['data-lazyload']
        pic_url = picUrl.split('data-lazyload="')[1].split('" title')[0]

        try:
            hotel_info_ctn = li.find("div", class_="hotel-info-ctn")
            hotel_info_main = hotel_info_ctn.find("div", class_="hotel-info-main")
            hotel_remark = hotel_info_ctn.find("div", class_="hotel-remark")
            link = hotel_info_main.find("a", class_="hotel-name-link")
            name = link.get_text()
            url = link['href']
            # mode = re.compile(r'\d+')
            # shopId = mode.search(url).group()
            # 截取数字
            shopId = int(re.sub(r'\D', "", url))

            detail_url = urlparse.urljoin(URL_FULL, url)
        except BaseException:
            continue
        # raise BaseException

        #         < p
        #
        #         class ="place" >
        #
        #         < i
        #
        #         class ="icon-position" > < / i >
        #
        #         < a
        #         data - midas - extends = "module=5_hotellist_region"
        #         href = "/hongkong/hotel/r2827"
        #         onclick = "_hip.push(['mv',{module:'5_hotellist_region', action: 'click',content:'/hotel/2827',note:'region_queryValue'}]);" > 尖沙咀 < / a >
        #     ， < span
        #
        #     class ="walk-dist" title="步行至九龙站2分钟" > 步行至九龙站2分钟 < / span >
        #
        # < / p >
        try:
            place = hotel_info_main.find("p", class_="place")
            addr = place.find("a").get_text()
            walk = place.find("span").get_text()
        except BaseException, e:
            addr = "无"
            walk = "无"
        # < p
        #
        # class ="hotel-tags" >
        #
        # < span > 豪华型 < / span >
        # < span > 风景不错 < / span >
        # < span > 很干净 < / span >
        # < span > 位置好 < / span >
        # < span > 交通方便 < / span >
        # < span > 游泳池赞 < / span >
        # < span > 服务好 < / span >
        # < / p >

        hotel_tags = hotel_info_main.find("p", class_="hotel-tags").find_all("span")
        tag_list = []
        for tag in hotel_tags:
            tag_list.append(tag.get_text().strip())

        price = hotel_remark.find("div", class_="price").get_text()
        star = hotel_remark.find("span")["title"]
        review_num = hotel_remark.find("a", class_="comments").get_text()

        ids.append(shopId)
        names.append(name.strip().replace("\n", ""))
        detail_urls.append(detail_url.strip().replace("\n", ""))
        addrs.append(addr.strip().replace("\n", ""))
        walks.append(walk.strip().replace("\n", ""))
        tags.append(tag_list)
        picUrls.append(pic_url)
        # 需要将 price unicode转str
        p_str = price.encode('utf-8')
        # print p_str
        try:
            p_int = int(filter(str.isdigit, p_str))
        except BaseException, e:
            # print e
            # print "价格获取失败，正常！"
            p_int = 0
        # print p_int
        prices.append(p_int)
        stars.append(star.strip().replace("\n", ""))

        try:
            review_num_int = int(review_num.strip().replace("\n", "").replace("(", "").replace(")", ""))
        except BaseException, e:
            print e
            review_num_int = 0
        review_nums.append(review_num_int)

    try:
        next_url = soup.find("div", class_="page").find("a", text='下一页')['href']
        next_url = urlparse.urljoin(PAGE_URL, next_url)
        url_manager.add_new_url(next_url)
    except:
        print "parse complete"

    return ids, names, detail_urls, addrs, walks, tags, prices, stars, review_nums, picUrls


def hotel_shop_parser(doc):
    try:
        soup = BeautifulSoup(doc, "lxml")

        base = soup.find("div", class_="base-info")
        addr = base.find("span", class_="hotel-address").get_text() + " " + base.find("span",
                                                                                      class_="hotel-metro").get_text()
        # tel = base.find("span", class_="call-number").get_text()
        hotel_info_ul_lis = soup.find("div", class_="hotel-info").find("ul", class_="list-info").find_all("li")

        index = 1
        for li in hotel_info_ul_lis:
            value = (li.find("div", class_="info-value"))
            if index == 1:
                tel = value.get_text()
            elif index == 2:
                openTime = value.get_text()
            elif index == 3:
                checkTime = value.get_text()

            elif index == 4:
                facs = []
                for span in value.find_all("span"):
                    facs.append(span.get_text().strip())
            elif index == 5:
                services = []
                for span in value.find_all("span"):
                    services.append(span.get_text().strip())
            elif index == 6:
                room_facs = []
                for span in value.find_all("span"):
                    room_facs.append(span.get_text().strip())
            elif index == 7:
                info = value.get_text()
            index += 1

        # tel_ = hotel_info_ul.find("div", text="联系方式：")
        # tel = tel_.next_sibling.next_sibling.get_text()
        #
        # openTime_ = hotel_info_ul.find("div", text="开业装修时间: ")
        # # openTime = openTime_.next_sibling.get_text()
        #
        # checkTime_ = hotel_info_ul.find("div", text="入离店时间: ")
        # # checkTime = checkTime_.next_sibling.get_text()
        #
        # facs_ = hotel_info_ul.find("div", text="酒店设施: ")
        # facs = []
        # for span in facs_.next_sibling.find_all("span"):
        #     facs.append(span.get_text().strip())
        #
        # room_facs_ = hotel_info_ul.find("div", text="房间设施: ")
        # room_facs = []
        # for span in room_facs_.next_sibling.find_all("span"):
        #     room_facs.append(span.get_text().strip())
        #
        # services_ = hotel_info_ul.find("div", text="酒店服务: ")
        # services = []
        # for span in services_.next_sibling.find_all("span"):
        #     services.append(span.get_text().strip())
        #
        # info_ = hotel_info_ul.find("div", text="酒店简介: ")
        # info = info_.next_sibling.get_text()
        review_num = -1
        try:
            review_count = soup.find("div", class_="hotel-all-appraise").find("a").find("span",
                                                                                        class_="hotel-scope-title").get_text()
            review_num = int(review_count.strip().replace("\n", "").replace("(", "").replace(")", ""))
        except BaseException, e:
            print e

        return addr, tel, openTime, checkTime, facs, room_facs, services, info, review_num
    except BaseException, e:
        print e


# def crawling_room(soup):
#     print "crawling_room()"
#     rooms = []
#     beds = []
#     breakfasts = []
#     nets = []
#     cancels = []
#     prices = []
#
#     # 此处信息是异步加载的，获取不到
#     room_list = soup.find("ul", class_="room-type-list").find_all("li")
#     print room_list
#     for li in room_list:
#         # 每个li是一个房型
#         room_style = li.find("div", class_="title").find("h3").get_text()
#         print room_style
#         for r in li.find("div", class_="roomlist").find_all("div", class_="room"):
#             room = room_style
#             rooms.append(room)
#             bed = r.find("div", class_="dph-col dph-col2").get_text()
#             breakfast = r.find("div", class_="dph-col dph-col3").get_text()
#             net = r.find("div", class_="dph-col dph-col4").get_text()
#             cancel = r.find("div", class_="dph-col dph-col5").get_text()
#             price = r.find("div", class_="dph-col dph-col6").get_text()
#             prices.append(price)


def get_room(doc_list, shopId):
    """获取每个酒店房型的详细信息"""

    # bedTypes = []
    # breakfasts = []
    # netTypes = []
    # cancelRules = []
    # prices = []
    # price0 = []

    rooms_info_total = []
    for doc in doc_list:
        index = doc_list.index(doc)

        try:

            room_list = json.loads(doc)["data"]["hotelGoodsList"]["roomList"]
        except BaseException, e:
            print e
            print "获取酒店房型详情失败"
            return
        else:
            n = room_list.__len__()
            if (n == 0):
                print "房型信息为空"
                return
            else:
                print "成功获取房型"
                roomId_list = []
                room_infos = []
                for room in room_list:
                    roomId = room["roomId"]
                    if roomId_list.__contains__(roomId):
                        continue
                    roomId_list.append(roomId)
                    title = room["title"]
                    price = room["price"]
                    # print roomId, title
                    # roomIds.append(roomId)
                    # shopIds.append(shopId)
                    # titles.append(title)
                    # prices.append(price)
                    room_info = {"roomId": roomId, "roomInfo": [roomId, shopId, title, price]}
                    room_infos.append(room_info)
        room_in_doc = [room_infos, index]
        rooms_info_total.append(room_in_doc)


        # for good in room["goodsList"]:
        #     bedType = good["bedType"]
        #     breakfast = good["breakfast"]
        #     netType = good["netType"]
        #     cancelRule = good["cancelRule"]
        #     price = good["price"]
        #
        #     shopIds.append(shopId)
        #     roomIds.append(roomId)
        #     titles.append(title)
        #     bedTypes.append(bedType)
        #     breakfasts.append(breakfast)
        #     netTypes.append(netType)
        #     cancelRules.append(cancelRule)
        #     prices.append(price)
        #
        #     print bedType, breakfast, netType, cancelRule, price
        # return shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices

    return rooms_info_total


def get_next_review_url(doc, url, shopId):
    soup = BeautifulSoup(doc, "lxml")
    try:
        next = soup.find("div", class_="Pages")
        nextpage = next.find("a", class_="NextPage")['href']
    except BaseException, e:
        print "find nextpage faile"
        global shopId_num

        shopId_num += 1
        print "第'%d'shopId '%d'已到末页" % (shopId_num, shopId)
        fo = open(
            r"D:\Liuchao\PycharmProjects\pythonproject\spider\dianping_hotel_hk\complete\'%s'num'%d'shopId '%d'complete.txt" % (
                today_str.shopId_num, shopId), "wb")
        fo.write(doc)
        fo.close()
    else:
        nextpage = urlparse.urljoin(url, nextpage)
        indentify_url = nextpage.split("shop")[1]
        url_manager.add_new_review_url(indentify_url)


def get_review_page_num(doc, url):
    try:
        url_mini = url.split("?")[0]
        shopId = int(re.sub(r'\D', "", url_mini))
    except BaseException, e:
        print e
        print traceback.format_exc()
        print "get_review()  ---shopId解析失败---------- url:", url
        shopId = 0
    soup = BeautifulSoup(doc, "lxml")

    totalpage_num = 1
    try:
        next = soup.find("div", class_="Pages")
        nextpage = next.find("a", class_="NextPage")
        lastpage = nextpage.previous_sibling.previous_sibling
        totalpage_num = int(lastpage['data-pg'])
    except BaseException, e:
        print "get_review_page_num(doc,url)", e
    return totalpage_num


def get_hotel_review(doc, url):
    try:
        url_mini = url.split("?")[0]
        shopId = int(re.sub(r'\D', "", url_mini))
    except BaseException, e:
        print e
        print traceback.format_exc()
        print "get_review()  ---shopId解析失败---------- url:", url
        shopId = 0
    # url_mini = url.split("?")[0]
    # shopId = int(re.sub(r'\D', "", url_mini))

    shopIds = []
    review_ids = []
    user_ids = []
    reviewStars = []
    rooms = []
    locs = []
    services = []
    healths = []
    facs = []
    comment_txts = []
    create_times = []
    likes = []
    reply_nums = []

    try:
        soup = BeautifulSoup(doc, "lxml")
        u = url_manager.new_review_urls
    except BaseException, e:
        print e
    # nextpage_full = "http://www.dianping.com/shop/3715216/review_more?pageno=210"

    # 找下一页的连接
    # 现在按照评论总页数来做循环，不需要找下一页的连接了
    # get_next_review_url(doc, url, shopId)

    # 解析页面内容
    try:
        comment_list = soup.find("div", class_="comment-list").find("ul").find_all("li", recursive=False)
    except BaseException, e:
        print e
        return
    for li in comment_list:
        try:
            review_id = int(li["data-id"])
            pic = li.find("div", class_="pic")
            user_id = int(pic.find("a")["user-id"])
            content = li.find("div", class_="content")
            star = content.find("div", class_="user-info").find("span")["title"]
            star1 = star
            reviewStar = -1
            star = star.encode("utf-8")
            if (u"非常好" == star1):
                reviewStar = 5
                pass
            elif ("很好" == star):
                reviewStar = 4
            elif ("好" == star):
                reviewStar = 3
            elif ("一般" == star):
                reviewStar = 2
            elif ("很差" == star):
                reviewStar = 1

            # 非常好4 很好3 好2 一般1 很差0
            comment_rst = content.find("div", class_="comment-rst").find_all("span")
            rsts = {"房间": None, "位置": None, "服务": None, "卫生": None, "设施": None}
            for rst in comment_rst:
                c = rst.get_text()
                value = int(re.sub(r'\D', "", c))
                key = re.sub(r'\d', "", c).split("(")[0].encode("utf-8")
                list = ["房间", "位置", "服务", "卫生", "设施"]
                if key not in list:
                    print "key not in list!!!!!!!!!!!!!!!!!!!!!", key

                rsts[key] = value

            room = -1
            loc = -1
            service = -1
            health = -1
            fac = -1
            if (rsts["房间"] != None):
                room = rsts["房间"]
            if (rsts["位置"] != None):
                loc = rsts["位置"]
            if (rsts["服务"] != None):
                service = rsts["服务"]
            if (rsts["卫生"] != None):
                health = rsts["卫生"]
            if (rsts["设施"] != None):
                fac = rsts["设施"]

            comment_txt = content.find("div", class_="comment-txt").find("div",
                                                                         class_="J_brief-cont").get_text().strip()
            misc_info = content.find("div", class_="misc-info")
            review_time = misc_info.find("span", class_="time").get_text()[0:8]
            r_time = review_time.split(u"更")[0].strip()

            l = r_time.__len__()
            y = datetime.date.today().strftime("%Y")
            century = "20"
            if l == 5:
                r_time = y + "-" + r_time
            elif l == 8:
                r_time = century + r_time
            else:
                # 异常情况
                r_time = u"0000-00-00"
            create_time = datetime.datetime.strptime(r_time, '%Y-%m-%d')

            countWrapper = misc_info.find("span", class_="col-right").find("span", class_="countWrapper")
            heart = countWrapper.find("a").find("span", class_="heart-num")
            like = -1
            if heart != None:
                like = int(re.sub(r'\D', "", heart.get_text()))

            reply = (countWrapper.next_sibling.next_sibling.find("span", class_="J_rtl"))
            reply_num = -1
            if reply != None:
                reply_num = int(reply.get_text())

        except BaseException, e:
            print e
            print traceback.format_exc()
            print "get_review(doc, url)中解析页面内容出现异常"
            print url
            print "shopId", shopId
            print "reviewId", review_id

            # 出现异常时 给剩余变量赋值
            reviewStar = room = loc = service = health = fac = like = reply_num = -2
            comment_txt = "此条评论信息未完整获取"
            create_time = datetime.datetime.strptime(u"1946-01-01", '%Y-%m-%d')
        try:
            shopIds.append(shopId)
            review_ids.append(review_id)
            user_ids.append(user_id)
            reviewStars.append(reviewStar)
            rooms.append(room)
            locs.append(loc)
            services.append(service)
            healths.append(health)
            facs.append(fac)
            comment_txts.append(comment_txt)
            create_times.append(create_time)
            likes.append(like)
            reply_nums.append(reply_num)

            result = [shopIds, review_ids, user_ids, reviewStars, rooms, locs, services, healths, facs, comment_txts,
                      create_times, likes, reply_nums]
        except BaseException, e:
            print e
    try:
        return result
    except BaseException, e:
        print e


def get_attraction_num(doc):
    try:
        soup = BeautifulSoup(doc, "lxml")
    except BaseException, e:
        print "in get_attraction_num(doc)"
        print e
    left = soup.find("div", class_='section-filter').find("div", class_="left").get_text()
    num = int(re.sub(r'\D', "", left))
    return num


def get_attraction_list(doc):
    shopIds = []
    picUrls = []
    tips = []
    try:
        soup = BeautifulSoup(doc, "lxml")
    except BaseException, e:
        print "in get_attraction_list(doc)"
        print e
    poi_list = soup.find("div", class_="poi-ctn").find("ul", class_="poi-list clearfix")
    for poi in poi_list.find_all("li"):
        a = poi.find("a")
        shopId = a['href'].split("shop/")[1]
        picUrl = a.find("img")['src']
        tip = poi.find("div", class_="poi-tips").get_text()

        shopIds.append(shopId)
        picUrls.append(picUrl)
        tips.append(tip)

    return shopIds, picUrls, tips

# TODO
def attraction_hotel_parser(doc):
    try:
        soup = BeautifulSoup(doc, "lxml")
        basic = soup.find("div", class_="basic-info")

    except BaseException, e:
        print e
        print "in attraction_hotel_parser(doc)"