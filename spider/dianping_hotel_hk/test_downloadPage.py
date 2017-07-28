from unittest import TestCase
import html_download

class TestDownloadPage(TestCase):
    def test_downloadPage(self):
        url = "http://www.baidu.com"
        doc = html_download.downloadPage(url)
        print doc
        # print ip_port
