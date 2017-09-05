# coding=utf-8

import dao

new_urls = set()
old_urls = set()

new_shop_urls = set()
old_shop_urls = set()

new_room_urls = set()
old_room_urls = set()

new_review_urls = set()
old_review_urls = set()


def add_new_url(url):
    if url is None:
        return
    if url not in new_urls and url not in old_urls:
        new_urls.add(url)


def add_new_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_urls.add(url)


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
        new_shop_urls.add(url)


def has_new_shop_url():
    return len(new_shop_urls) != 0


def get_new_shop_url():
    new_shop_url = new_shop_urls.pop()
    old_shop_urls.add(new_shop_url)
    return new_shop_url


def add_new_shop_url(url):
    if url is None:
        return
    if url not in new_shop_urls and url not in old_shop_urls:
        new_shop_urls.add(url)


def add_new_shop_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_shop_urls.add(url)


def has_new_shop_url():
    return len(new_shop_urls) != 0


def get_new_shop_url():
    new_shop_url = new_shop_urls.pop()
    old_shop_urls.add(new_shop_url)
    return new_shop_url


# 房间详情的url列表

def add_new_room_url(url):
    if url is None:
        return
    if url not in new_room_urls and url not in old_room_urls:
        new_room_urls.add(url)


def add_new_room_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_room_urls.add(url)


def has_new_room_url():
    return len(new_room_urls) != 0


def get_new_room_url():
    new_room_url = new_room_urls.pop()
    old_room_urls.add(new_room_url)
    return new_room_url


# 评论详情的url列表

def add_new_review_url(url):
    if url is None:
        print url
        u = url
        print u
        return
    if url not in new_review_urls and url not in old_review_urls:
        new_review_urls.add(url)
        print "new review_url add"
        u2 = new_review_urls
        pass
        x = new_review_urls
        # print u2


def remove_old_review_urls(url):
    old_review_urls.remove(url)


def add_new_review_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_review_urls.add(url)


def has_new_review_url():
    return len(new_review_urls) != 0


def get_new_review_url():
    urls = new_review_urls
    new_review_url = new_review_urls.pop()
    url = str(new_review_url)
    old_review_urls.add(url)
    # dao.add_review_url_crawled(url)
    return url


def print_new_review_url():
    for url in new_review_urls:
        print url


def insert_new_review_url_into_db():
    dao.insert_new_review_url(new_review_urls)
