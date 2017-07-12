# coding:utf8
import urllib2

"""Html下载器"""


class HtmlDownloader(object):
    @staticmethod
    def download(url):
        """
        下载该页面
        :param url:
        :return:
        """
        if url is None:
            return None
        # 打开一个url，返回一个http：client.HttpResponse
        response = urllib2.urlopen(url)

        # 若请求失败
        if response.getcode() != 200:
            return None
        return response.read()
