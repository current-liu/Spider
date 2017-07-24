from unittest import TestCase
import html_download
import html_parser


class TestGet_review(TestCase):
    def test_get_review(self):
        REVIEW_URL = "http://www.dianping.com/shop/3715216/review_more"
        shopId = 3715216
        doc = html_download.downloadPage(REVIEW_URL)
        print doc

        # soup = html_parser.get_review(doc, shopId)
