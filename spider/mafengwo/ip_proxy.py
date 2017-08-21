# coding=utf-8

import random
import time
import json
import requests

ip_pool = []
url = "http://http-webapi.zhimaruanjian.com/getip?num=3&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1"
url_IPProxyPool = "http://127.0.0.1:8000/?types=0&count=50"
dict_ip_to_remove = {}


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
                print "getting ip, please wait..."
                time.sleep(1.5)
            else:
                break
        except BaseException, e:
            # print e
            msg2 = "there is a exception, wait for try again"
            print msg2

    ip_pool += ip_list
    res = "ok"
    return res


def download_from_ip_pool():
    """向IPProxyPool发请求"""
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
            doc = requests.get(url_IPProxyPool).content
            ip_list = json.loads(doc)
            if ip_list.__len__() == 0:
                print "getting ip, please wait..."
                time.sleep(1.5)
            else:
                break
        except BaseException, e:
            # print e
            msg2 = "there is a exception, wait for try again"
            print msg2

    ip_pool += ip_list
    res = "ok"
    return res


def get_ip():
    """获得一个随机Ip"""
    global ip_pool

    while True:
        n = ip_pool.__len__()
        # TODO 正常运行时改为20
        if n >= 10:
            break
        msg = download_ips()
        if msg == "fail":
            msg1 = "fail to get ip, please handle"
            print msg1
            raise BaseException

    data = random.choice(ip_pool)
    ip = data['ip']
    port = data['port']
    ip_port = ip + ":" + str(port)

    return ip_port


def get_ip_from_IPProxyPool():
    """获得一个随机Ip"""
    global ip_pool

    while True:
        n = ip_pool.__len__()
        if n >= 20:
            break
        msg = download_from_ip_pool()
        if msg == "fail":
            msg1 = "fail to get ip, please handle"
            print msg1
            raise BaseException

    data = random.choice(ip_pool)
    ip = data[0]
    port = data[1]
    ip_port = ip + ":" + str(port)

    return ip_port


def remove_ip(ip_port, error_num=3):
    """移除无法使用的ip,error_num为该ip下载失败几次时删除"""
    global dict_ip_to_remove

    ip = ip_port.split(":")[0]

    if dict_ip_to_remove.__contains__(ip):
        if dict_ip_to_remove[ip] <= error_num:
            dict_ip_to_remove[ip] += dict_ip_to_remove[ip] + 1
        else:
            for i in ip_pool:
                if i["ip"] == ip:
                    ip_pool.remove(i)
                    break
    else:
        dict_ip_to_remove[ip] = 1
