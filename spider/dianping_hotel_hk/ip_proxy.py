# coding=utf-8
import random
import time

import html_download
import json
import requests
import dao

url_list = []
url = "http://http-webapi.zhimaruanjian.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1"


# def get_ips_from_db():
#     d = dao.select_ip()
#     data = list(d)
#     return data
#
#
# def load_ip_and_insert():
#     doc = requests.get(url).content
#     data_s = json.loads(doc)['data']
#     for data in data_s:
#         ip = data['ip']
#         port = data['port']
#         d = [ip, port]
#         dao.insert_ip(d)
#     pass


def get_ips():
    doc = requests.get(url).content
    ip_list = json.loads(doc)['data']
    if ip_list.__len__() == 0:
        print "正在获取代理ip，请等待"
        time.sleep(1.5)
        ip_list = get_ips()

    # if ip_list.__len__() < 5:
    #     ip_list += get_ip()
    #
    # data = random.choice(ip_list)
    # ip = data['ip']
    # port = data['port']
    # ip_port = ip + ":" + str(port)

    return ip_list

