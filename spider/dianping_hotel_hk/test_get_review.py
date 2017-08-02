from unittest import TestCase
from dianping_hotel_hk import html_download
from dianping_hotel_hk import h_parser

REVIEW_URL = "http://www.dianping.com/shop/6276819/review_more"
class TestGet_review(TestCase):
    # def setUp(self):
    #
    #     doc = html_download.downloadPage(self.REVIEW_URL)
    #     shopId = 3715216



    # def test_get_review_page_num(self):
    #     REVIEW_URL = "http://www.dianping.com/shop/6276819/review_more"
    #     doc, msg = html_download.downloadPage(REVIEW_URL)
    #     num = h_parser.get_review_page_num(doc, REVIEW_URL)
    #     print num

    def test_get_review(self):
        REVIEW_URL = "http://www.dianping.com/shop/3052915/review_more?pageno=15"
        doc, msg = html_download.downloadPage(REVIEW_URL)
        num = h_parser.get_review(doc, REVIEW_URL)
        print num
