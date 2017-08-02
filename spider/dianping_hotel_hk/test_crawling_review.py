from unittest import TestCase
import h_parser
import html_download
import result_manager
import dao


class TestCrawling_review(TestCase):
    def test_crawling_review(self):
        url = "http://www.dianping.com/shop/4567116/review_more"
        url1 = "http://www.dianping.com/shop/21136114/review_more?pageno=2"

        doc, msg = html_download.downloadPage(url1)
        result = h_parser.get_review(doc, url1)
        if result:
            result_manager.add_new_result(result)
            dao.insert_hotel_review()
