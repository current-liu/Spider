# coding:utf8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_content):
        """
        解析页面
        :param page_url:
        :param html_content:
        :return:
        """
        if page_url is None or html_content is None:
            return
        # html.parser 是Python的内置标准库；也可以考虑用lxml
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        # 打印一下 soup 对象的内容，格式化输出
        # print soup.prettify()
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):
        """
        获取页面中所有符合检验规则的url
        :param page_url:
        :param soup:
        :return:
        """
        new_urls = set()
        # /item/Hadoop
        links = soup.find_all('a', href=re.compile(r"/item/\w+"))  # 正则表达式
        for link in links:
            new_url = link['href']
            # 这个方法会将new_url按照page_url的格式拼接成新的url
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}  # 这是个字典

        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>×××</h1></dd>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        t = type(title_node)
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
