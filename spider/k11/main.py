# coding=utf-8
import parser
import download


def main():
    GOAL_URL = "http://www.shanghaik11.com/index.php?m=content&c=index&a=lists&catid=90"
    doc = download.download_page(GOAL_URL)
    soup = parser.html_parser(doc)
    print doc


if __name__ == "__main__":
    main()
