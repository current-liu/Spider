from unittest import TestCase
import ip_proxy

class TestGet_ips(TestCase):
    # def test_get_ips(self):
    #     url = ip_proxy.get_ips()
    #     print url

    def test_load_ip(self):
        # while True:
        #     ip_proxy.load_ip()
        # print "test_load_ip"
        data = ip_proxy.get_ips()
        pass
