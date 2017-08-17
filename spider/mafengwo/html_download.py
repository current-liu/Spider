# coding=utf-8
import datetime
import requests
import random
import ip_proxy

headers1 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
headers2 = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
headers3 = {'User-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)'}
headers4 = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3'}
headers5 = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 '}
h_total = [headers1, headers2, headers3, headers4, headers5]
h = random.choice(h_total)

today = datetime.date.today()
today_fo = today.strftime("%Y%m%d")
filename = today_fo+".txt"


def downloadPage(url, fo_log):
    flag = True
    index = 0
    while (flag):
        index += 1
        print "download第%s次" % index, url
        # 同一个地址最多尝试6次
        max_try = 8
        if index == max_try:
            msg5 = "放弃：" + url
            print msg5
            fo_log.write(msg5)
            break

        error_num = 3
        ip_port = ip_proxy.get_ip()
        # OR
        # error_num = 1
        # ip_port = ip_proxy.get_ip_from_IPProxyPool()

        proxies = {'http': ip_port}

        # 处理请求结果
        doc = ""
        try:
            doc = requests.get(url, headers=h, proxies=proxies, timeout=3).content
            pass
        except BaseException, e:
            print e
            msg = "download error"
        else:
            msg = "ok"
            if doc.__contains__("403 Forbidden") or doc == "":
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


def downloadPage_without_proxy(url, fo_log):
    flag = True
    index = 0
    while (flag):
        index += 1
        print "download第%s次" % index, url
        # 同一个地址最多尝试3次
        max_try = 3
        if index == max_try:
            msg5 = "放弃：" + url
            print msg5
            fo_log.write(msg5)
            break

        # 处理请求结果
        doc = ""
        try:
            doc = requests.get(url, headers=h, timeout=3).content
            pass
        except BaseException, e:
            print e
            msg = "download error"
        else:
            msg = "ok"
            if doc.__contains__("403 Forbidden") or doc == "":
                msg = "403 Forbidden"
            elif doc.__contains__("<h1>ERROR</h1>") or doc.__contains__("ERROR") or doc.__contains__("doc with error"):
                msg = "ERROR"

        # 请求成功，跳出循环
        try:
            if msg == "ok":
                break
        except BaseException, e:
            print e

    return doc, msg



