# coding=utf-8

from bs4 import BeautifulSoup


def html_parser(doc):
    soup = BeautifulSoup(doc, "html.parser")
    ul = soup.find("ul", class_="ideas_tit")

    return soup
