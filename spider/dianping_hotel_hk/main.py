# coding=utf-8
import html_parser
import html_download
import url_manager
import output


def main():
    print "begin"
    GOAL_URL = "http://www.dianping.com/hongkong/hotel/r2827"
    url_manager.add_new_url(GOAL_URL)
    # doc = html_download.downloadPage(GOAL_URL)
    # soup = html_parser.htmlParser(doc)
    # print doc

    ids = []
    names = []
    detail_urls = []
    addrs = []
    walks = []
    tags = []
    prices = []
    stars = []
    review_nums = []


    while (url_manager.has_new_url()):
        url = url_manager.get_new_url()
        print url
        doc = html_download.downloadPage(url)
        shop_id, name, detail_url, addr, walk, tag, price, star, review_num = html_parser.htmlParser(doc)
        # print content
        ids += shop_id
        names += name
        detail_urls += detail_url
        addrs += addr
        walks += walk
        tags += tag
        prices += price
        stars += star
        review_nums += review_num

    for (i, n, d, a, w, t, p, s, r) in zip(ids, names, detail_urls, addrs, walks, tags, prices, stars, review_nums):
        print i, n, d, a, w, t, p, s, r
        tags = " ".join(t)
        output.insert(i, n, d, a, w, tags, p, s, r)


if __name__ == "__main__":
    main()
