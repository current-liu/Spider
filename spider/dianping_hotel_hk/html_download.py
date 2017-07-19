# coding=utf-8

import requests

import pip
# print(pip.pep425tags.get_supported())


def downloadPage(url):
    data = requests.get(url).content
    return data
