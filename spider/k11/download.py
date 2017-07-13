# coding=utf-8

import requests




def download_page(url):
    data = requests.get(url).content
    return data
