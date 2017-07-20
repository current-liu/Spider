# coding=utf-8

new_urls = set()
old_urls = set()

new_shop_urls = set()
old_shop_urls = set()


def add_new_url(url):
    if url is None:
        return
    if url not in new_urls and url not in old_urls:
        new_urls.add(url)


def add_new_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_urls.add_new_url(url)


def has_new_url():
    return len(new_urls) != 0


def get_new_url():
    new_url = new_urls.pop()
    old_urls.add(new_url)
    return new_url


def add_new_shop_url(url):
    if url is None:
        return
    if url not in new_shop_urls and url not in old_shop_urls:
        new_shop_urls.add(url)


def add_new_shop_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_shop_urls.add_new_shop_url(url)


def has_new_shop_url():
    return len(new_shop_urls) != 0


def get_new_shop_url():
    new_shop_url = new_shop_urls.pop()
    old_shop_urls.add(new_shop_url)
    return new_shop_url