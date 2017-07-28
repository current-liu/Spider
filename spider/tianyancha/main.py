# coding=utf-8
import h_parser
import html_download
import url_manager
import output
import traceback
import time
import random
from openpyxl import Workbook


def main():
    print "begin"
    keyword = "%E6%96%B9%E5%BE%97"
    GOAL_URL = "https://www.tianyancha.com/search?key=" + keyword + "&checkFrom=searchBox"
    url_manager.add_new_url(GOAL_URL)
    # doc = html_download.downloadPage(GOAL_URL)
    # soup = html_parser.htmlParser(doc)
    # print doc

    wb = Workbook()
    dest_filename = '方得.xlsx'.decode("utf-8")
    ws1 = wb.active
    ws1.title = "方得".decode("utf-8")

    while (url_manager.has_new_url()):
        try:
            url = url_manager.get_new_url()
            print "while 1 ", url
            doc = html_download.downloadPage(url)
            company_urls = h_parser.htmlParser(doc)
            url_manager.add_new_company_urls(company_urls)
        except BaseException, e:
            print "while 1"
            print e
            print traceback.format_exc()

    time.sleep(2)

    company_name_s = []
    contact_s = []
    company_human_s = []
    details_s = []

    index_2 = 0
    while (url_manager.has_new_company_url()):
        t = random.uniform(2, 3)
        print "random ", t
        time.sleep(t)
        index_2 += 1
        print index_2
        if (index_2 == 5):
            break
        try:
            url = url_manager.get_new_company_url()
            print "while 2", url
            doc = html_download.downloadPage1(url)
            company_name, contact, company_human, details = h_parser.company_html_parser(doc)
            print company_name
            print contact
            print company_human
            print details
            company_name_s.append(company_name)
            contact_s.append(contact)
            company_human_s.append(company_human.decode("utf-8"))
            details_s.append(details.decode("utf-8"))



        except BaseException, e:
            print "while 2"
            print e
            print traceback.format_exc()

    for (i, m, o, p) in zip(company_name_s, contact_s, company_human_s, details_s):
        print i, m, o, p
        index = company_name_s.index(i) + 1
        print index
        col_A = 'A%s' % index
        col_B = 'B%s' % index
        col_C = 'C%s' % index
        col_D = 'D%s' % index
        print col_A, col_B, col_C, col_D
        ws1[col_A] = i
        ws1[col_B] = m
        ws1[col_C] = o
        ws1[col_D] = p
    wb.save(filename=dest_filename)


if __name__ == "__main__":
    main()
