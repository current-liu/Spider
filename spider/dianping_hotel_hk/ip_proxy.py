# coding=utf-8

import random
import time
import json
import requests


ip_pool = []
url = "http://http-webapi.zhimaruanjian.com/getip?num=3&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1"


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


def download_ips():
    """向芝麻代理发请求"""
    global ip_pool
    index = 1
    flag = True

    while (flag):
        # 尝试10次失败后，返回错误信息，由get_ip()抛出异常
        index += 1
        if index == 10:
            res = "fail"
            return res
        try:
            doc = requests.get(url).content
            ip_list = json.loads(doc)['data']
            if ip_list.__len__() == 0:
                print "正在获取代理ip，请稍后"
                time.sleep(1.5)
            else:
                break
        except BaseException, e:
            # print e
            msg2 = "获取代理ip异常，正在重试"
            print msg2

    ip_pool += ip_list
    res = "ok"
    return res


def get_ip():
    """获得一个随机Ip"""
    global ip_pool

    while True:
        n = ip_pool.__len__()
        if n >= 5:
            break
        msg = download_ips()
        if msg == "fail":
            msg1 = "获取代理ip失败，请处理"
            print msg1
            raise BaseException

    data = random.choice(ip_pool)
    ip = data['ip']
    port = data['port']
    ip_port = ip + ":" + str(port)

    return ip_port


def remove_ip(ip_port):
    """移除无法使用的ip"""
    ip = ip_port.split(":")[0]
    for i in ip_pool:
        if i["ip"] == ip:
            ip_pool.remove(i)
            break


