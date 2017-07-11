# -*- codiing:utf-8 -*-

from weare_spider import Download, Parser
from datetime import date, datetime, timedelta
import time
import random
import logging


class SpiderMainMain(object):
    def __init__(self):
        self.download = Download.Download(logger)
        self.parser = Parser.Parser()

    def start(self):
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")
        tenago = now - timedelta(hours=1)
        # now = datetime.strptime("2016-12-25 00:00:00", "%Y-%m-%d %H:%M:%S")
        # tenago = datetime.strptime("2016-11-15 00:00:00", "%Y-%m-%d %H:%M:%S")
        flag = True
        page = 0
        while flag != False:
            page = page + 1
            response_page = self.download.title_download(page)
            # 得到的就是在上一次爬取到现在有变动的的帖子
            title_list, flag = self.parser.title_parse(response_page, now, tenago)
            for title_url in title_list:
                # 因为得到一个有关的言论就要插入一个,所以在parser里面进行实时插入
                self.download.reply_download(title_url, now, tenago)
        self.download.output.close()
        print("success!")


if __name__ == "__main__":
    index = r'http://weare.hk/bbs/forumdisplay.php?fid=13'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=datetime.now().strftime("%Y%m%d%H%M%S") + '.log',
                        filemode='w')
    logger = logging.getLogger()
    spider_main = SpiderMainMain()
    while True:
        spider_main.start()
        time.sleep(3600)
