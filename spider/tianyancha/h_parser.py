# coding=utf-8

from bs4 import BeautifulSoup
import re
import traceback
import url_manager


def htmlParser(doc):
    soup = BeautifulSoup(doc, "lxml")

    try:
        """获取下一页的url"""
        next_page = soup.find("li", class_="pagination-next ng-scope ")
        n_p_url = next_page.find("a")['href']
        url_manager.add_new_url(n_p_url)
    except BaseException, e:
        print e, "htmlParser(doc)"
        print traceback.format_exc()

    ul = soup.find("div", class_="b-c-white search_result_container")
    company_urls = []

    for li in ul.find_all("div", recursive=False):
        # print li.get_text().strip()
        # print "------------------------------------------"

        url = li.find("div", class_="col-xs-10 search_repadding2 f18").find("a")['href']
        company_urls.append(url)

    return company_urls


def company_html_parser(doc):
    soup = BeautifulSoup(doc, "lxml")
    company_header = soup.find("div", class_="company_header_width ie9Style")
    company_name = company_header.find("span", class_="f18 in-block vertival-middle").get_text().strip()
    contact_infos = company_header.find("div", class_="f14 new-c3 mt10").find_all("span")
    contact = ""
    for span in contact_infos:
        contact = contact + "_" + span.get_text().strip()
    company_info_table = soup.find("table", class_="table companyInfo-table text-center f14")
    company_human = company_info_table.find("div",
                                            class_="company-human-box position-rel in-block vertical-top text-left float-left point").get_text()
    details = soup.find("div", class_="row b-c-white base2017").get_text().strip()

    company_human_s = company_human.encode("utf-8").replace("\n", "").replace(" ", "")
    details_s = details.encode("utf-8").replace("\n", "").replace(" ", "")
    contact_s = contact
    # print company_name
    # print contact_s
    # print company_human_s
    # print details_s
    return company_name, contact_s, company_human_s, details_s
