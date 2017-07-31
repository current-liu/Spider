# coding=utf-8
from unittest import TestCase
import h_parser
import html_download
from bs4 import BeautifulSoup
import json
import time
import datetime


class TestGet_room(TestCase):
    def setUp(self):
        self.url_shop = "http://www.dianping.com/shop/3715216"
        self.url_getroom = "http://www.dianping.com/hotelproduct/pc/hotelPrepayAndOtaGoodsList?shopId=3715216&" \
                           "checkinDate=2017-08-02&checkoutDate=2017-08-03"
        self.doc = html_download.downloadPage(self.url_shop)
        soup = BeautifulSoup(self.doc, "lxml")


    def test_get_room(self):
        self.doc = html_download.downloadPage(self.url_getroom)
        data  = json.loads(self.doc)
        room_list = data["data"]["hotelGoodsList"]["roomList"]
        for room in room_list:
            print room["roomId"], room["title"]
            # for good in room["goodsList"]:
            #     print good["bedType"], good["breakfast"], good["netType"], good["cancelRule"], good["price"]

    # def test_checkindate(self):
    #     today = datetime.date.today()
    #     tomorrow = today + datetime.timedelta(days=1)
    #     checkinDate = today.strftime("%Y-%m-%d")
    #     checkoutDate = tomorrow.strftime("%Y-%m-%d")
    #
    #     print checkinDate