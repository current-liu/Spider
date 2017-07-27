# coding=utf-8
import h_parser
import html_download
import url_manager
import output
import traceback
import time


def main():
    print "begin"
    keyword = "%E6%96%B9%E5%BE%97"
    GOAL_URL = "https://www.tianyancha.com/search?key=" + keyword + "&checkFrom=searchBox"
    url_manager.add_new_url(GOAL_URL)
    # doc = html_download.downloadPage(GOAL_URL)
    # soup = html_parser.htmlParser(doc)
    # print doc

    while (url_manager.has_new_url()):
        try:
            url = url_manager.get_new_url()
            print url
            doc = html_download.downloadPage(url)
            company_urls = h_parser.htmlParser(doc)
            url_manager.add_new_company_urls(company_urls)
        except BaseException, e:
            print "while 1"
            print e
            print traceback.format_exc()

    # time.sleep(1000)

    while (url_manager.has_new_company_url()):
        try:
            url = url_manager.get_new_company_url()
            doc = html_download.downloadPage1(url)
            company_name, contact, company_human, details = h_parser.company_html_parser(doc)
            print company_name
            print contact
            print company_human
            print details
        except BaseException, e:
            print "while 2"
            print e
            traceback.format_exc()


if __name__ == "__main__":
    main()
