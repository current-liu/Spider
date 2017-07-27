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


def add_new_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_urls.add(url)


new_company_urls = set()
old_company_urls = set()


def add_new_company_url(company_url):
    if company_url is None:
        return
    if company_url not in new_company_urls and company_url not in old_company_urls:
        new_company_urls.add(company_url)


def has_new_company_url():
    return len(new_company_urls) != 0


def get_new_company_url():
    new_company_url = new_company_urls.pop()
    old_company_urls.add(new_company_url)
    return new_company_url


def add_new_company_urls(urls):
    if urls is None or len(urls) == 0:
        return
    for url in urls:
        new_company_urls.add(url)
