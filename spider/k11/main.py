# coding=utf-8
import html_parser
import html_download
import url_manager
import output


def main():
    print "begin"
    GOAL_URL = "http://www.shanghaik11.com/index.php?m=content&c=index&a=lists&catid=90"
    url_manager.add_new_url(GOAL_URL)
    # doc = html_download.downloadPage(GOAL_URL)
    # soup = html_parser.htmlParser(doc)
    # print doc

    pic_urls = []
    emoji_names = []
    create_times = []
    contents = []
    labels = []
    replys = []

    while (url_manager.has_new_url()):
        url = url_manager.get_new_url()
        print url
        doc = html_download.downloadPage(url)
        pic_url, emoji_name, create_time, content, label, reply = html_parser.htmlParser(doc)
        # print content

        pic_urls += pic_url
        emoji_names += emoji_name
        create_times += create_time
        contents += content
        labels += label
        replys += reply

    for (p, e, c, ct, l, r) in zip(pic_urls, emoji_names, create_times, contents, labels, replys):
        print p, e, c, ct, l, r
        output.insert(p, e, c, ct, l, r)


if __name__ == "__main__":
    main()
