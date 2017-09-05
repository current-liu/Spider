from unittest import TestCase
import dianping_hk.dao

class TestGet_last_old_review_urls(TestCase):
    def test_get_last_old_review_urls(self):
        r = dianping_hk.dao.select_new_review_urls()
        print r
