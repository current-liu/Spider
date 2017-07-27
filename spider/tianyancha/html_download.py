# coding=utf-8

import requests

import pip
# print(pip.pep425tags.get_supported())


def downloadPage(url):
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url,headers=headers1).content
    return data
