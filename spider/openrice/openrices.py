# -*-coding:utf-8 -*-
import re
import time
import urlparse
import urllib2
import pymysql
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def download(url):
    print 'Downloading:',url
    try:
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}

        request = urllib2.Request(url, headers=headers)
        html = urllib2.urlopen(request).read()
        # print html
    except urllib2.URLError as e:
        print 'Download error:',e.reason
        html = None
    time.sleep(20)
    return html

def shopinfo(root_url):
    categories=''
    payment=''
    shopstar=0
    html=download(root_url)
    soup=BeautifulSoup(html,"html.parser",from_encoding='utf-8')
    name=soup.find('div',{'class':'poi-name'})
    shopname=name.h1.span.text
    star=soup.find('div',{'class':'header-score'})
    if star:
        shopstar = float(star.text)
    smiley=soup.findAll('div',{'class':'score-div'})
    smiley_smiley=smiley[0].text
    smiley_ok=smiley[1].text
    smiley_cry=smiley[2].text
    mark=soup.find('div',{'class':'header-bookmark-count'})
    shopmark=mark.text
    location=soup.find('div',{'class':'header-poi-district dot-separator'})
    district=location.a.text
    range=soup.find('div',{'class':'header-poi-price dot-separator'})
    pricerange=range.a.text
    cate=soup.find('div',{'class':'header-poi-categories dot-separator'})
    if cate:
        cate=cate.find_all('div')
        for j in cate:
            categories=categories+','+j.text
        categories=categories[1:]
    else:
        categories=''
    address=soup.find('div',{'class':'address-info-section'})
    if address:
        shopaddress = address.text[102:]
    else:
        shopaddress=''
    tel=soup.find('section',{'class':'telephone-section'})
    if tel:
        shoptel = tel.text[6:]
    else:
        shoptel=''
    intro=soup.find('div',{'class':'content js-text-wrapper'})
    if intro:
        a = len(intro.text)
        introduction = intro.text[:a - 6]
    else:
        introduction=''
    hour=soup.find('section',{'class':'opening-hours-and-normal-notice-section'})
    if hour:
        shophours = hour.text[5:]
    else:
        shophours=''
    pay=soup.find('div',{'class':'comma-tags'})
    if pay:
        pay=pay.find_all('span')
        for i in pay:
            payment=payment+','+i.text
        payment=payment[1:]
    else:
        payment=''
    return shopname,shopstar,smiley_smiley,smiley_ok,smiley_cry,shopmark,district,pricerange,categories,shopaddress,shoptel,introduction,shophours,payment
# 获取店铺Id
def Id(url):
    i=len(url)-1
    while i>0:
        if url[i]=='r':
            break
        else:
            i=i-1
    return url[i+1:]
# 获取用户Id
def userid(url):
    i=len(url)-1
    while i>0:
        if url[i]=='=':
            break
        else:
            i=i-1
    return url[i+1:]
# 获取评论id
def reviewid(url):
    i=len(url)-1
    while i>0:
        if url[i]=='e':
            break
        else:
            i=i-1
    return url[i+1:]

def trans1(a):
    b=a.replace(' 瀏覽','')
    return b
def trans2(a):
    b=a.replace(' 讚好','')
    return b
def trans3(a):
    b=a.replace(' 留言','')
    return b
def trans4(a):
    b=a.replace(' ','')
    return b
def trans6(a):
    b=a.replace('\n','')
    return b
def trans7(a):
    b=a.replace('\r','')
    return b
# 计算用户加入openrice的时间
def trans5(a):
    # print a
    # print len(a)
    s=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    # print s
    if len(a)==2:
        # print int(s[5:7])
        # print int(s[0:4])
        if int(s[5:7])-int(a[1])<=0:
            year=int(s[0:4])-1-int(a[0])
            mon=int(s[5:7])+12-int(a[1])
        if int(s[5:7])-int(a[1])>0:
            year=int(s[0:4])-int(a[0])
            mon=int(s[5:7])-int(a[1])
    if len(a)==1:
        if int(s[5:7])-int(a[0])<=0:
            year=int(s[0:4])-1
            mon=int(s[5:7])+12-int(a[0])
        if int(s[5:7])-int(a[0])>0:
            year=int(s[0:4])
            mon=int(s[5:7])-int(a[0])
    if mon<10:
        return str(year) + '0'+str(mon) + '01'
    else:
        return str(year) + str(mon) + '01'
# 获取每一页中评论的链接
def review_link(url):
    html = download(url)
    soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
    link=soup.findAll('div',{'class':'review-title'})
    for i in range(len(link)):
        link[i]=link[i].a['href']
        # print link[i]
        d = 'https://www.openrice.com'
        link[i] = urlparse.urljoin(d, link[i])
        # print link[i]
    return link

def next_link (url):
    html = download(url)
    soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
    link=soup.find('a',{'class':'pagination-button next js-next'})
    if link:
        link = link['href']
        d = 'https://www.openrice.com'
        link = urlparse.urljoin(d, link)
        return link



aaa=time.strftime('%Y-%m-%d', time.localtime(time.time()))
def reviewesinfo(url):
    user_id=''
    url_user=''
    html = download(url)
    soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
    # 评论id
    reviewId = reviewid(url)
    # 评论时间
    review_time=aaa
    time= soup.find('span', {'itemprop': 'datepublished'})
    # print len(time.text)
    if len(time.text)>8:
        review_time = time.text
    # else:
    #     mm = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    #     print mm
    #     review_time=str(mm)



    # 评论浏览量
    views_count=0
    views= soup.find('span', {'class': 'view-count'})
    if views:
        views_count = views.text
        views_count = re.sub('\D', '', views_count)
    # 标题内容
    title = soup.find('div', {'class': 'review-title'})
    titles=title.text
    # 评论内容
    contents=''
    content = soup.find('section', {'class': 'review-container'})
    if content:
        contents = content.text
    # print content
    # 用户编号和名称
    user = soup.find('div', {'class': 'name'})
    if user:
        username = user.text
        try:
            if user.a['href']:
                userId = user.a['href']
                user_id = userid(userId)
                d = 'https://www.openrice.com'
                url_user = urlparse.urljoin(d, userId)
        except: KeyError
    # 用户感受
    smiley=''
    smile = soup.find('div', {'class': 'icon or-sprite-inline-block common_smiley_ok_60x60_desktop'})
    if smile:
        smiley='ok'
    else:
        smile = soup.find('div', {'class': 'icon or-sprite-inline-block common_smiley_smile_60x60_desktop'})
        if smile:
            smiley = 'smiley'
        else:
            smile = soup.find('div', {'class': 'icon or-sprite-inline-block common_smiley_cry_60x60_desktop'})
            if smile:
                smiley = 'cry'
    # 味道、环境、服务、卫生等的评分
    comment=soup.findAll('div', {'class': 'stars js-stars'})
    comments=[0,0,0,0,0]
    for i in range(len(comment)):
        a=comment[i].find_all('span', {'class': 'or-sprite-inline-block common_yellowstar_desktop'})
        comments[i]=len(a)
    # 用餐日期
    mealdate='0001-01-01'
    date=soup.find('div', {'class': 'date text'})
    if date:
        if len(date.text)>8:
            mealdate = date.text
    # 用餐途径，用餐时段，人均消费
    diningpathway=''
    consumption=''
    mealtime=''
    way=soup.find('section', {'class': 'info-section detail'})
    if way:
        pathway = way.find_all('div', class_='text')
        if pathway:
            for a in pathway:
                s = a['class']
                if len(s) == 1:
                    if len(a.text) < 4:
                        # print len(a.text)
                        diningpathway = a.text
                else:
                    continue
        time = way.find_all('div', class_='price text')
        if time:
                for d in time:
                    if len(d.text) < 3:
                        mealtime = d.text
                    else:
                        mealtime = ''
                        consumption = d.text
    #推介数量
    recommend=0
    rmd=soup.find('div', {'class': 'recommend-user-count-container'})
    if rmd:
        r = rmd.find('span', {'class': 'js-count'})
        recommend=int(r.text)
    return reviewId,review_time,int(views_count),titles,contents,user_id,username,smiley,comments,mealdate,diningpathway,mealtime,consumption,recommend,url_user
# 获取用户信息
def userinfo(url):
    actionzone=''
    workplace=''
    residence=''
    favoritefood=''
    first_ = 0
    vipre = 0
    follownum=0
    badeg=''
    fansnum=0

    html = download(url)
    soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
    # 徽章等级
    badge=soup.find('div', {'class': 'txt_13 MT5'})
    if badge:
        badge = badge.text
    # 关注量
    follows=soup.find('div', {'class': 'sprite-myor_bg_following inline_block'})
    if follows:
        follow = follows.find('div', {'class': 'count'})
        if follow:
            follownum = follow.text
    # 粉丝数量
    fans = soup.find('div', {'class': 'sprite-myor_bg_follower inline_block'})
    if fans:
        fan = fans.find('div', {'class': 'count'})
        if fan:
            fansnum = fan.text
    # 写过的评论数量
    rev=soup.findAll('a',{'data-myor-tab':'Review'})
    # print rev
    # revnum=rev.find('div',{'class':'count'})
    revnum=0
    # 加入openrice的时间
    regTime='00010101'
    reg=soup.find('div',{'class':"ML10 MR10 txt_12 PT5"})
    if reg:
        reg = reg.find('div', {'class': 'ML25'})
        if reg:
            reg = reg.text
            regT = reg
            # print regT
            # print regT[8]
            reg = reg.split('年', 1)
            # print len(reg)
            now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if regT[-1] == '月':
                for i in range(len(reg)):
                    reg[i] = re.sub('\D', '', reg[i])
                regTime = trans5(reg)
            if regT[-1] == '年':
                for i in range(len(reg)):
                    # print reg[i]
                    reg[i] = re.sub('\D', '', reg[i])
                    # print reg[i]
                    y = int(now[0:4]) - int(reg[0])
                regTime = str(y) + now[5:7] + '01'


    # 经常出没的范围
    first=''
    viprecommend=''
    about=soup.findAll('div',{'class':'MB10 PT5 dash_border'})
    if about:
        for s in about:
            zone = s.findAll('div', {'class': 'MT5'})
            for h in zone:
                # print h.div['class']
                if h.span['class'] == [u'sprite-myor_icon_location', u'MR5', u'FL', u'v_align_middle']:
                    zones = h.findAll('a')
                    if zones:
                        for b in zones:
                            actionzone = actionzone + b.text + ','
                if h.span['class'] == [u'sprite-myor_icon_work', u'MR5', u'FL', u'v_align_middle']:
                    zones = h.find('a')
                    if zones:
                        workplace = zones.text
                if h.span['class'] == [u'sprite-myor_icon_home', u'MR5', u'FL', u'v_align_middle']:
                    zones = h.find('a')
                    if zones:
                        residence = zones.text
                if h.span['class'] == [u'sprite-myor_icon_cuisine', u'MR5', u'FL', u'v_align_middle']:
                    food = h.find('div', {'class': 'ML25'})
                    if food:
                        favoritefood = food.div.text
                if h.div['class'] == [u'FL', u'statics_block']:
                    aa = h.find('div', {'class': 'FL statics_block'})
                    first = aa.text
                    VR = h.find('div', {'class': 'FL statics_block MT5'})
                    if VR:
                        viprecommend = VR.text
                if h.div['class'] == [u'FL', u'statics_block',u'MT5']:
                    VR = h.find('div', {'class': 'FL statics_block MT5'})
                    viprecommend = VR.text

                if len(first):
                    first = re.sub('\D', '', first)
                    first_=int(first)
                if len(viprecommend):
                    viprecommend = re.sub('\D', '', viprecommend)
                    vipre=int(viprecommend)

    return badge,follownum,fansnum,revnum,regTime,actionzone,workplace,residence,favoritefood,first_,vipre


while 1:
    db = pymysql.connect(host='192.168.1.166', user='root', passwd='keystone', db='dpark', charset='utf8')
    cursor = db.cursor()
    cursor.execute('SET NAMES utf8mb4')
    cursor.execute('set GLOBAL max_allowed_packet=67108864')
    root_url = [
        # 'https://www.openrice.com/zh/hongkong/r-%E7%86%8A%E5%B0%8F%E9%A4%A8-%E8%8D%83%E7%81%A3-%E8%A5%BF%E5%BC%8F-r471788',
        # 'https://www.openrice.com/zh/hongkong/r-%E6%BB%BF%E5%B1%8B%E5%BB%9A%E6%88%BF-%E8%8D%83%E7%81%A3-%E5%A4%9A%E5%9C%8B%E8%8F%9C-%E7%94%9C%E5%93%81-%E7%B3%96%E6%B0%B4-r462187',
        # 'https://www.openrice.com/zh/hongkong/r-chefs-stage-kitchen-%E8%8D%83%E7%81%A3-%E8%A5%BF%E5%BC%8F-all-day-breakfast-r519423',
        # 'https://www.openrice.com/zh/hongkong/r-outback-steakhouse-%E8%8D%83%E7%81%A3-%E6%BE%B3%E6%B4%B2%E8%8F%9C-r193875',
        # 'https://www.openrice.com/zh/hongkong/r-delifrance-%E8%8D%83%E7%81%A3-%E6%B3%95%E5%9C%8B%E8%8F%9C-%E6%B2%99%E5%BE%8B-r620',
        # 'https://www.openrice.com/zh/hongkong/r-%E9%B3%A5%E5%B1%B1%E5%90%8D-%E8%8D%83%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-%E6%8B%89%E9%BA%B5-r463244',
        # 'https://www.openrice.com/zh/hongkong/r-%E7%BF%94%E9%BE%8D%E6%8B%89%E9%BA%B5%E5%B0%8F%E7%B1%A0%E5%8C%85-%E8%8D%83%E7%81%A3-%E6%BB%AC%E8%8F%9C-%E4%B8%8A%E6%B5%B7-%E9%9B%B2%E5%90%9E-%E9%A4%83%E5%AD%90-r172715',
        # 'https://www.openrice.com/zh/hongkong/r-%E6%9C%83%E6%89%801%E8%99%9F-%E6%84%89%E8%8A%B1%E5%9C%92-%E8%8D%83%E7%81%A3-%E7%B2%B5%E8%8F%9C-%E5%BB%A3%E6%9D%B1-%E9%BB%9E%E5%BF%83-r493408',
        # 'https://www.openrice.com/zh/hongkong/r-%E7%89%9B%E9%99%A3-%E8%8D%83%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-%E6%97%A5%E5%BC%8F%E6%94%BE%E9%A1%8C-r171038',
        # 'https://www.openrice.com/zh/hongkong/r-%E5%BF%85%E5%8B%9D%E5%AE%A2-%E8%8D%83%E7%81%A3-%E6%84%8F%E5%A4%A7%E5%88%A9%E8%8F%9C-%E8%96%84%E9%A4%85-r19594',
        # 'https://www.openrice.com/zh/hongkong/r-%E5%A4%A2%E8%A6%8B%E5%B1%8B-%E8%8D%83%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-r459557',
        # 'https://www.openrice.com/zh/hongkong/r-crostini-bakery-cafe-%E8%8D%83%E7%81%A3-%E8%A5%BF%E5%BC%8F-%E9%BA%B5%E5%8C%85%E5%BA%97-r437955',
        # 'https://www.openrice.com/zh/hongkong/r-burger-bus-%E8%8D%83%E7%81%A3-%E8%A5%BF%E5%BC%8F-%E6%BC%A2%E5%A0%A1%E5%8C%85-r468127',
        # 'https://www.openrice.com/zh/hongkong/r-%E6%98%9F%E5%B7%B4%E5%85%8B%E5%92%96%E5%95%A1-%E8%8D%83%E7%81%A3-%E7%BE%8E%E5%9C%8B%E8%8F%9C-%E6%B2%99%E5%BE%8B-r18908',
        # 'https://www.openrice.com/zh/hongkong/r-%E4%B8%80%E7%B2%A5%E9%BA%B5-%E8%8D%83%E7%81%A3-%E6%B8%AF%E5%BC%8F-%E7%B2%A5%E5%93%81-r486371',
        # 'https://www.openrice.com/zh/hongkong/r-%E9%BB%91%E7%A6%8F%E5%A4%9A%E6%8B%89%E9%BA%B5-%E8%8D%83%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-%E6%8B%89%E9%BA%B5-r164083',
        # 'https://www.openrice.com/zh/hongkong/r-%E9%BA%A5%E7%95%B6%E5%8B%9E-%E8%8D%83%E7%81%A3-%E7%BE%8E%E5%9C%8B%E8%8F%9C-%E6%BC%A2%E5%A0%A1%E5%8C%85-r479134',
        # 'https://www.openrice.com/zh/hongkong/r-%E4%BB%8A%E5%8A%A9%E6%97%A5%E6%9C%AC%E6%96%99%E7%90%86-%E8%8D%83%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-r179360',
        # 'https://www.openrice.com/zh/hongkong/r-pokka-cafe-grill-specialist-%E8%8D%83%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-r164076',
        # 'https://www.openrice.com/zh/hongkong/r-%E5%A4%A7%E5%AE%B6%E6%A8%82-%E8%8D%83%E7%81%A3-%E6%B8%AF%E5%BC%8F-r466152',
        # 'https://www.openrice.com/zh/hongkong/r-%E7%AF%89%E5%9C%B0%E5%A3%BD%E5%8F%B8-%E8%8D%83%E7%81%A3-%E6%97%A5%E6%9C%AC%E8%8F%9C-%E5%A3%BD%E5%8F%B8-%E5%88%BA%E8%BA%AB-r27012',
        # 'https://www.openrice.com/zh/hongkong/r-%E5%A5%87%E8%8F%AF%E9%A4%85%E5%AE%B6-%E8%8D%83%E7%81%A3-%E6%B8%AF%E5%BC%8F-%E5%94%90%E9%A4%85-r9517',
        # 'https://www.openrice.com/zh/hongkong/r-%E8%81%96%E5%AE%89%E5%A8%9C%E9%A4%85%E5%B1%8B-%E8%8D%83%E7%81%A3-%E6%B8%AF%E5%BC%8F-%E9%BA%B5%E5%8C%85%E5%BA%97-r37630',
        # 'https://www.openrice.com/zh/hongkong/r-%E5%9A%90%E5%91%B3-%E8%8D%83%E7%81%A3-%E6%B8%AF%E5%BC%8F-%E7%B2%89%E9%BA%B5-%E7%B1%B3%E7%B7%9A-r480486', 
		
        'https://www.openrice.com/zh/hongkong/r-paul-lafayet-%E5%B0%96%E6%B2%99%E5%92%80-%E6%B3%95%E5%9C%8B%E8%8F%9C-%E8%A5%BF%E5%BC%8F%E7%B3%95%E9%BB%9E-r39176',
		'https://www.openrice.com/zh/hongkong/r-atum-restaurant-%e5%b0%96%e6%b2%99%e5%92%80-%e8%a5%bf%e5%bc%8f-%e6%b5%b7%e9%b2%9c-r470070',
		'https://www.openrice.com/zh/hongkong/r-pan-de-pain-pancakes-sweets-%e5%b0%96%e6%b2%99%e5%92%80-%e6%97%a5%e6%9c%ac%e8%8f%9c-%e7%94%9c%e5%93%81-%e7%b3%96%e6%b0%b4-r482866',
		'https://www.openrice.com/zh/hongkong/r-%e9%81%93%e9%a1%bf%e5%a0%80%e5%be%a1%e5%a5%bd%e7%83%a7%e4%b8%93%e9%97%a8%e5%ba%97-%e5%b0%96%e6%b2%99%e5%92%80-%e6%97%a5%e6%9c%ac%e8%8f%9c-%e9%93%81%e6%9d%bf%e7%83%a7-r515663',
		'https://www.openrice.com/zh/hongkong/r-%e5%a4%a7%e9%83%bd%e7%83%a4%e9%b8%ad-%e5%b0%96%e6%b2%99%e5%92%80-%e7%b2%a4%e8%8f%9c-%e5%b9%bf%e4%b8%9c-r75985',
		'https://www.openrice.com/zh/hongkong/r-%e7%89%a7%e7%be%8a%e5%b0%91%e5%b9%b4%e5%88%9b%e6%84%8f%e5%92%96%e5%95%a1%e9%a6%86-by-gabee-%e5%b0%96%e6%b2%99%e5%92%80-%e8%a5%bf%e5%bc%8f-all-day-breakfast-r483416',
		'https://www.openrice.com/zh/hongkong/r-gochiso-%e5%b0%96%e6%b2%99%e5%92%80-%e6%97%a5%e6%9c%ac%e8%8f%9c-%e6%b5%b7%e9%b2%9c-r187500',
		'https://www.openrice.com/zh/hongkong/r-smile-yogurt-dessert-bar-%e5%b0%96%e6%b2%99%e5%92%80-%e8%a5%bf%e5%bc%8f-%e9%9b%aa%e7%b3%95-%e4%b9%b3%e9%85%aa-r185590',
		'https://www.openrice.com/zh/hongkong/r-the-butchers-club-burger-%e5%b0%96%e6%b2%99%e5%92%80-%e7%be%8e%e5%9b%bd%e8%8f%9c-%e6%b1%89%e5%a0%a1%e5%8c%85-r479740',
		'https://www.openrice.com/zh/hongkong/r-%e9%87%8e%e7%8e%a9%e7%94%b0%e5%ba%97-%e5%b0%96%e6%b2%99%e5%92%80-%e5%a4%9a%e5%9b%bd%e8%8f%9c-%e6%9e%9c%e6%b1%81-r518824',
		'https://www.openrice.com/zh/hongkong/r-%e6%9c%9d%e8%8a%b1%e5%a4%95%e6%8b%be-%e5%b0%96%e6%b2%99%e5%92%80-%e6%97%a5%e6%9c%ac%e8%8f%9c-all-day-breakfast-r519409',
		'https://www.openrice.com/zh/hongkong/r-wired-green-%e5%b0%96%e6%b2%99%e5%92%80-%e6%97%a5%e6%9c%ac%e8%8f%9c-r480964',
		'https://www.openrice.com/zh/hongkong/r-agnes-b-le-pain-grille-%e5%b0%96%e6%b2%99%e5%92%80-%e6%b3%95%e5%9b%bd%e8%8f%9c-%e6%b5%b7%e9%b2%9c-r180361',
		'https://www.openrice.com/zh/hongkong/r-%e9%9c%9e%e5%b0%8f%e9%a3%9e-%e5%b0%96%e6%b2%99%e5%92%80-%e6%b2%aa%e8%8f%9c-%e4%b8%8a%e6%b5%b7-%e7%83%a7%e8%85%8a-r486350',
		'https://www.openrice.com/zh/hongkong/r-%e5%ae%8f-%e6%97%a5%e6%9c%ac%e7%94%9c%e5%93%81%e5%ba%97-%e5%b0%96%e6%b2%99%e5%92%80-%e6%97%a5%e6%9c%ac%e8%8f%9c-%e7%94%9c%e5%93%81-%e7%b3%96%e6%b0%b4-r156670',
		'https://www.openrice.com/zh/hongkong/r-%e7%82%8e%e4%b8%b8%e5%b1%85%e9%85%92%e5%b1%8b-%e5%b0%96%e6%b2%99%e5%92%80-%e6%97%a5%e6%9c%ac%e8%8f%9c-%e5%af%bf%e5%8f%b8-%e5%88%ba%e8%ba%ab-r486357'

		]


    for url in root_url:
        review = []
        next = []
        shopName, shopStar, smiley_smiley, smiley_ok, smiley_cry, shopmark, district, priceRange, categories, shopAddress, shopTel, introduction, shopHours, payment = shopinfo(url)
        shopId = Id(url)
        # print shopName, shopStar, smiley_smiley, smiley_ok, smiley_cry, shopmark, district, priceRange, categories, shopAddress, shopTel, introduction, shopHours, payment
        sql = 'REPLACE INTO openrice_shops (shopId,shopName,shopStar,smiley_smiley,smiley_ok,smiley_cry,shopmark,district,priceRange,categories,shopAddress,shopTel,introduction,shopHours,payment) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (
            shopId, shopName, shopStar, smiley_smiley, smiley_ok, smiley_cry, shopmark, district, priceRange,
            categories,
            shopAddress, shopTel, introduction, shopHours, payment))
        db.commit()
        url = url + '/reviews'
        next.append(url)
        for url1 in next:
            links = review_link(url1)
            for ss in links:
                review.append(ss)
            if next_link(url1):
                next.append(next_link(url1))
            # i = 0
            # while i < 3:
            for url2 in review:
                userId = ""
                url_user = ''
                sql1 = 'REPLACE INTO openrice_reviewes(revieweId,shopId,creatTime,views,title,content,userId,userName,smiley,taste,environment,services,health,quality,mealdate,diningpathway,mealtime,consumption,recommend) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                reviewId, creattime, views, title, content, userId, userName, smiley, comments, mealdate, way, mealtime, consumption, recommend, url_user = reviewesinfo(
                    url2)

                taste = comments[0]
                environment = comments[1]
                services = comments[2]
                health = comments[3]
                quality = comments[4]
                content = trans4(trans3(trans2(trans1(content))))
                content = re.sub('[0-9]', '', content)
                content = content.replace('\n', '')
                content = content.replace('\r', '')
                # print repr(content)
                # print reviewId, shopId, creattime, views, title, content, userId, userName, smiley, taste, environment, services, health, quality, mealdate, way, mealtime, consumption, recommend, url_user
                param = (
                    reviewId, shopId, creattime, views, title, content, userId, userName, smiley, taste, environment,
                    services, health, quality, mealdate, way, mealtime, consumption, recommend)
                cursor.execute(sql1, param)
                db.commit()
                # 获取用户信息
                if url_user:
                    badge, follows, fans, revnum, regTime, actionzone, workplace, residence, favorite, firstWritten, VipRecommend = userinfo(
                        url_user)
                    # print
                    # badge, follows, fans, revnum, regTime, actionzone, workplace, residence, favorite, firstWritten, VipRecommend
                    sql2 = 'REPLACE INTO openrice_user (userId,userName,badge,follows,fans,revNum,regTime,actionZone,workPlace,residence,favorite,firstWritten,vipRecommend) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    cursor.execute(sql2, (
                        userId, userName, badge, follows, fans, revnum, regTime, actionzone, workplace, residence,
                        favorite,
                        firstWritten, VipRecommend))
                    db.commit()
                # for url2 in review:


    time.sleep(86400)
