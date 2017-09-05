from unittest import TestCase
import dianping_hk.ip_proxy
from dianping_hk import html_download


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

    # def test_ip_proxy(self):
    #     url = "http://www.baidu.com"
    #     # ip = ip_proxy.get_ip()
    #     html_download.downloadPage(url)

    def test_get_ip_from_IPProxyPool(self):
        # ip_port = ip_proxy.get_ip_from_IPProxyPool()
        # proxies = {'http': ip_port}
        while(True):
            url = "http://www.dianping.com"
            doc, msg = html_download.downloadPage(url)
            pass
