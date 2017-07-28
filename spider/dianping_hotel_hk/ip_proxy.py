# coding=utf-8

import html_download
import json
import requests
import dao

url_list = []
url = "http://http-webapi.zhimaruanjian.com/getip?num=2&type=2&pro=&city=0&yys=0&port=1&time=2&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2"


def get_ips():
    d = dao.select_ip()
    data = list(d)
    return data


def load_ip():
    doc = requests.get(url).content
    data_s = json.loads(doc)['data']
    for data in data_s:
        ip = data['ip']
        port = data['port']
        d = [ip, port]
        dao.insert_ip(d)
    pass
