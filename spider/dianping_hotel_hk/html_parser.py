# coding=utf-8

from bs4 import BeautifulSoup
import re
import url_manager
import urlparse


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
