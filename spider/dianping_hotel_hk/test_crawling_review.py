from unittest import TestCase
import h_parser
import html_download
import result_manager
import dao
from dianping_hotel_hk.main import get_attraction_review_on_page


class TestCrawling_review(TestCase):
    # def test_crawling_review(self):
    #     url = "http://www.dianping.com/shop/4567116/review_more"
    #     url1 = "http://www.dianping.com/shop/21136114/review_more?pageno=2"
    #
    #     doc, msg = html_download.downloadPage(url1)
    #     result = h_parser.get_hotel_review(doc, url1)
    #     if result:
    #         result_manager.add_new_result(result)
    #         dao.insert_hotel_review()

    def test_get_attraction_review_on_page(self):
        get_attraction_review_on_page(2028214, 329)
