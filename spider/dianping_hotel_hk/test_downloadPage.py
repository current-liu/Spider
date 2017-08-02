from unittest import TestCase
from dianping_hotel_hk import html_download

class TestDownloadPage(TestCase):
    def test_downloadPage(self):
        url = "http://www.dianping.com/shop/3715216/review_more"
        url1 = "http://www.baidu.com"
        doc, msg = html_download.downloadPage(url)
        doc1, msg = html_download.downloadPage(url1)
        print doc
        # print ip_port
