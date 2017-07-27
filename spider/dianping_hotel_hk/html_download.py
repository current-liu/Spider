# coding=utf-8

import requests
import re
import random
import pip

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

header_list = [headers, headers1, headers_review]


def downloadPage(url):
    data = requests.get(url, headers=random.choice(header_list)).content

    # data = re.sub(r'\n', '', data)
    return data
