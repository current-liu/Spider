# coding=utf-8
import datetime
import os

import requests
import re
import random
import pip
import ip_proxy
import url_manager

# print(pip.pep425tags.get_supported())


headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "_hc.v=c6d30569-3f06-e4ba-45e1-5ddfae14840b.1500429443; s_ViewType=1; _lxsdk_cuid=15d599805c2c8-067d11a9b89f4f-333f5902-1fa400-15d599805c2c8; _lxsdk=15d599805c2c8-067d11a9b89f4f-333f5902-1fa400-15d599805c2c8; aburl=1; cy=341; cye=hongkong; __mta=210588202.1500429508159.1500598248467.1500599199420.17",
    "Host": "www.dianping.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

headers_review = {

    "Host": "www.dianping.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": "_hc.v=c6d30569-3f06-e4ba-45e1-5ddfae14840b.1500429443; _lxsdk_cuid=15d599805c2c8-067d11a9b89f4f-333f5902-1fa400-15d599805c2c8; _lxsdk=15d599805c2c8-067d11a9b89f4f-333f5902-1fa400-15d599805c2c8; s_ViewType=10; __mta=210588202.1500429508159.1500876527017.1500877703615.30; JSESSIONID=5F043D423BB9F464A0408361B7A0099A; aburl=1; cy=341; cye=hongkong; _lxsdk_s=15d7347e0f3-ab3-b79-60a%7C%7C3"

}

headers2 = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
headers3 = {
    'User-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)'}
headers4 = {
    'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3'}
headers5 = {
    'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 '}
h_total = [headers2, headers3, headers4, headers5]
h = random.choice(h_total)

today = datetime.date.today()
today_fo = today.strftime("%Y%m%d")
filename = today_fo+".txt"
os.chdir("./log")
fo_log = open(filename, "a")


def downloadPage(url):
    flag = True
    index = 0
    while (flag):
        index += 1
        print "download第%s次" % index, url
        # 同一个地址最多尝试6次
        max_try = 6
        if index == max_try:
            msg5 = "放弃：" + url
            print msg5
            fo_log.write(msg5)
            break

        # 获取随机IP,迁移到ip_proxy
        # try:
        #     global ip_list
        #     if ip_list.__len__() < 5:
        #         ip_list += ip_proxy.get_ips()
        #
        #     data = random.choice(ip_list)
        #     ip = data['ip']
        #     port = data['port']
        #     ip_port = ip + ":" + str(port)
        #     # print ip_port
        #
        #     proxies = {'http': ip_port}
        # except BaseException, e:
        #     print e

        # 获取随机IP
        # error_num为该ip下载失败几次时删除

        error_num = 3
        ip_port = ip_proxy.get_ip()
        # OR
        # error_num = 1
        # ip_port = ip_proxy.get_ip_from_IPProxyPool()

        proxies = {'http': ip_port}

        # 处理请求结果
        msg = "ok"
        doc = ""
        try:
            doc = requests.get(url, headers=h, proxies=proxies, timeout=2).content
            pass
        except BaseException, e:
            print e
            msg = "download error"
        else:
            if doc.__contains__("403 Forbidden"):
                msg = "403 Forbidden"
            elif doc.__contains__("<h1>ERROR</h1>") or doc.__contains__("ERROR") or doc.__contains__("doc with error"):
                msg = "ERROR"


        # 请求成功，跳出循环
        try:
            if msg == "ok":
                break
            else:
                # 移除无法使用的ip
                ip_proxy.remove_ip(ip_port, error_num)
        except BaseException, e:
            print e

    return doc, msg


def downloadPage_without_proxy(url):
    flag = True
    index = 0
    while (flag):
        index += 1
        print "download第%s次" % index, url
        # 同一个地址最多尝试3次
        max_try = 3
        if index == max_try:
            msg6 = "放弃：" + url
            print msg6
            fo_log.write(msg6)
            break

        # 处理请求结果
        msg = "ok"
        doc = ""
        try:
            doc = requests.get(url, headers=h, timeout=2).content
            pass
        except BaseException, e:
            print e
            msg = "download error"
        else:
            if doc.__contains__("403 Forbidden"):
                msg = "403 Forbidden"
            elif doc.__contains__("<h1>ERROR</h1>") or doc.__contains__("ERROR") or doc.__contains__("doc with error"):
                msg = "ERROR"

        # 请求成功，跳出循环
        if msg == "ok":
            break

    return doc, msg



