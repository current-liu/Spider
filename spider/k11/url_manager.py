# coding=utf-8

new_urls = set()
old_urls = set()


def add_new_url(url):
    if url is None:
        return
    if url not in new_urls and url not in old_urls:
        new_urls.add(url)


def has_new_url():
    return len(new_urls) != 0


def get_new_url():
    new_url = new_urls.pop()
    old_urls.add(new_url)
    return new_url


