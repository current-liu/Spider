# coding=utf-8

from bs4 import BeautifulSoup
import re
import url_manager
import urlparse
import json


def htmlParser(doc):
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

    for li in hotel_list.find_all("li", class_=" hotel-block J_hotel-block"):
        # print li.get_text()
        # print "------------------------------------------"
        # < a class ="hotel-name-link" data-midas-extends="module=5_hotellist_shop"
        # href = "/shop/3715216"
        # onclick = "_hip.push(['mv',{module:'5_hotellist_shop', action: 'click',content:'/shop/3715216',title:'香港丽思卡尔顿酒店'}]);"
        # target = "_blank"
        # title = "香港丽思卡尔顿酒店" > 香港丽思卡尔顿酒店 < / a >
        # < a class ="ibook" href="/shop/3715216" target="_blank" > < / a >

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
        place = hotel_info_main.find("p", class_="place")
        addr = place.find("a").get_text()
        walk = place.find("span").get_text()

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
        # 需要将 price unicode转str
        p_str = price.encode('utf-8')
        # print p_str
        try:
            p_int = int(filter(str.isdigit, p_str))
        except BaseException, e:
            print e
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

    return ids, names, detail_urls, addrs, walks, tags, prices, stars, review_nums


def shopParser(doc):
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

    return addr, tel, openTime, checkTime, facs, room_facs, services, info


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


def get_room(doc, shopId):
    """获取每个酒店房型的详细信息"""
    shopIds = []
    roomIds = []
    titles = []
    bedTypes = []
    breakfasts = []
    netTypes = []
    cancelRules = []
    prices = []

    try:
        room_list = json.loads(doc)["data"]["hotelGoodsList"]["roomList"]
    except BaseException, e:
        print e
        print "获取酒店房型详情失败"
    else:
        n = room_list.__len__()
        if (n == 0):
            print "房型信息为空"
        else:
            print "成功获取房型"
            for room in room_list:

                roomId = room["roomId"]
                title = room["title"]
                print roomId, title
                for good in room["goodsList"]:
                    bedType = good["bedType"]
                    breakfast = good["breakfast"]
                    netType = good["netType"]
                    cancelRule = good["cancelRule"]
                    price = good["price"]

                    shopIds.append(shopId)
                    roomIds.append(roomId)
                    titles.append(title)
                    bedTypes.append(bedType)
                    breakfasts.append(breakfast)
                    netTypes.append(netType)
                    cancelRules.append(cancelRule)
                    prices.append(price)

                    print bedType, breakfast, netType, cancelRule, price

    return shopIds, roomIds, titles, bedTypes, breakfasts, netTypes, cancelRules, prices


def get_review(doc, shopId):
    soup = BeautifulSoup(doc, "lxml")
    comment_list = soup.find("div", class_="comment-list").find("ul").find_all("li")
    for li in comment_list:
        review_id = li["data-id"]
        pic = li.find("div", class_="pic")
        user_id = pic.find("a")["user-id"]
        content = li.find("div", class_="content")
        star = content.find("div", class_="user-info").find("span")["title"]
        if(star):
            pass
