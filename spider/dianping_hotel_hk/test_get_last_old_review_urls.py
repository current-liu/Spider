from unittest import TestCase
import output

class TestGet_last_old_review_urls(TestCase):
    def test_get_last_old_review_urls(self):
        r = output.get_last_old_review_urls()
        print r
