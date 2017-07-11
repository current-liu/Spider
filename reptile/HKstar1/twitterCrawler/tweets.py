#  -*- coding: utf-8 -*-
import tweepy
import time
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tweepy import OAuthHandler

consumer_key = 'GnkYfPLb1J5SjlqAsMlnZbqoy'
consumer_secret = 'EsFbEtqli67W7vAv6noG3szzUilDYKzszZ2VLcmvibe2oiOpCZ'
access_token = '780406990845587456-YQxtvA8EeVyYiRBVBVuf9NnyQ6IkaWR'
access_secret = 'ao1W0wJCTaOjTejOZ4pb3kPoxMK5X1n2X1eJHAOWdEQn4'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth,proxy="127.0.0.1:1080",wait_on_rate_limit=True)

# db = pymysql.connect(host="202.110.49.146", user="root", passwd="Sz@860213", db="hkstar", charset="utf8")
db = pymysql.connect(host="192.168.1.20", user="root", passwd="root", db="hkstar", charset="utf8")
cursor = db.cursor()
user_name=['hoccgoomusic','pongnan','sabaocean','gangaotai','joshuawongcf','nathanlawkc','Suyutong','chenguoxiangcgx','JiangNao','kengelahk','Passiontimes','GaldenPolymer','galileo44']

## this is the latest starting tweet id
for name in user_name:
    lis=[]
    user_timeline = api.user_timeline(screen_name=name, count=1, include_retweets=True)
    for tweet in user_timeline:
        id = tweet.id
    lis.append(id)
    for i in range(0, 17):
        ## iterate through all tweets
        ## tweet extract method with the last list item as the max_id
        user_timeline = api.user_timeline(screen_name=name, count=200, max_id=lis[-1], include_retweets=True)
        # time.sleep(300)
        ## 5 minute rest between api calls
        sql = """INSERT IGNORE INTO tweets (status_id,created_at,message,user_id,user_name) VALUES (%s,%s,%s,%s,%s)"""
        print len(user_timeline)
        # user_timeline.pop(0)
        for tweet in user_timeline:
            cursor.execute(sql, (str(tweet.id), tweet.created_at, str(tweet.text), str(tweet.user.id),str(tweet.user.name)))
            db.commit()
            print ("ID:", tweet.id)
            print ("User ID:", tweet.user.id)
            print ("Text:", tweet.text)
            print ("Created:", tweet.created_at)
            print ("name:",tweet.user.name)
            # print ("in_reply_to_user_id:",tweet.in_reply_to_status_id)
            lis.append(tweet.id)
            print tweet

# timeline = api.user_timeline(screen_name='hoccgoomusic', include_rts=True,count=5)
# for tweet in timeline:
#     print ("ID:", tweet.id)
#     print ("User ID:", tweet.user.id)
#     print ("Text:", tweet.text)
#     print ("Created:", tweet.created_at)
