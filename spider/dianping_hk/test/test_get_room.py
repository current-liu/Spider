# coding=utf-8
from unittest import TestCase
import dianping_hk.h_parser
import dianping_hk.html_download
from bs4 import BeautifulSoup
import json
import time
import datetime


class TestGet_room(TestCase):
    def setUp(self):
        self.url_shop = "http://www.dianping.com/shop/3715216"
        self.url1 = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=67132351&" \
                    "checkinDate=2017-08-01&checkoutDate=2017-08-02"
        self.url2 = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=67132351&" \
                    "checkinDate=2017-08-02&checkoutDate=2017-08-03"
        self.url3 = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=67132351&" \
                    "checkinDate=2017-08-03&checkoutDate=2017-08-04"
        self.url4 = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=67132351&" \
                    "checkinDate=2017-08-04&checkoutDate=2017-08-05"
        self.url5 = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=67132351&" \
                    "checkinDate=2017-08-05&checkoutDate=2017-08-06"
        self.doc1, msg = dianping_hk.html_download.downloadPage(self.url1)
        self.doc2, msg = dianping_hk.html_download.downloadPage(self.url2)
        self.doc3, msg = dianping_hk.html_download.downloadPage(self.url3)
        self.doc4, msg = dianping_hk.html_download.downloadPage(self.url4)
        self.doc5, msg = dianping_hk.html_download.downloadPage(self.url5)
        self.doc_list = [self.doc1, self.doc2, self.doc3, self.doc4, self.doc5]
        # soup = BeautifulSoup(self.doc, "lxml")

    def test_get_room(self):
        dianping_hk.h_parser.get_room(self.doc_list, 67132351)
        # self.doc = html_download.downloadPage(self.url_getroom)
        # data  = json.loads(self.doc)
        # room_list = data["data"]["hotelGoodsList"]["roomList"]
        # for room in room_list:
        #     print room["roomId"], room["title"]
        # for good in room["goodsList"]:
        #     print good["bedType"], good["breakfast"], good["netType"], good["cancelRule"], good["price"]

        # def test_checkindate(self):
        #     today = datetime.date.today()
        #     tomorrow = today + datetime.timedelta(days=1)
        #     checkinDate = today.strftime("%Y-%m-%d")
        #     checkoutDate = tomorrow.strftime("%Y-%m-%d")
        #
        #     print checkinDate
