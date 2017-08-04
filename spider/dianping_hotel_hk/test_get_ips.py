from unittest import TestCase
import ip_proxy
from dianping_hotel_hk import html_download


class TestGet_ips(TestCase):
    # def test_get_ips(self):
    #     url = ip_proxy.get_ips()
    #     print url

    # def test_load_ip(self):
    #     # while True:
    #     #     ip_proxy.load_ip()
    #     # print "test_load_ip"
    #     data = ip_proxy.get_ips()
    #     pass

    def test_ip_proxy(self):
        url = "http://www.baidu.com"
        # ip = ip_proxy.get_ip()
        html_download.downloadPage(url)
