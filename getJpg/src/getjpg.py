# coding=utf-8
"""爬网页上的图片"""
import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# 百度图片 方得 首页
urlStr = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1499759781985_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%96%B9%E5%BE%97"

html = getHtml(urlStr)
print html

imgURL = "http://img0.imgtn.bdimg.com/it/u=2407965014,970115050&fm=26&gp=0.jpg"
imgURL1 = "http://cdn.duitang.com/uploads/item/201603/18/20160318075107_ZKHMA.thumb.700_0.jpeg"


def getImg(html):
    reg = re.compile('(http://[\S]*\.jpg|http://[\S]*\.jpeg)')
    imgList = re.findall(reg, html)
    # print "imgList:", imgList
    x = 0
    for imgurl in imgList:
        if imgurl.__contains__("gp=0"):
            print "gp=0 ", x, imgurl
        else:
            print x, imgurl
            urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1
# x = 0
# urllib.urlretrieve(imgURL1, '%s.jpg' % x)
# #     return imgList
# # print getImg(html)
# #

getImg(html)

