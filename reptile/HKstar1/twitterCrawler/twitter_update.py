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
db = pymysql.connect(host="192.168.1.20", user="root", passwd="root", db="hkstar",port=3306, charset="utf8mb4")
cursor = db.cursor()
user_name=['hoccgoomusic','pongnan','sabaocean','gangaotai','joshuawongcf','nathanlawkc','Suyutong','chenguoxiangcgx','JiangNao','kengelahk','Passiontimes','GaldenPolymer','galileo44']
sql = """REPLACE INTO tweets (status_id,created_at,message,user_id,user_name) VALUES (%s,%s,%s,%s,%s)"""
while 1:
    status_id = []
    for name in user_name:
        try:
            user_timeline = api.user_timeline(screen_name=name, count=5, include_retweets=True)
            for tweet in user_timeline:
                cursor.execute(sql, (
                    str(tweet.id), tweet.created_at, str(tweet.text), str(tweet.user.id), str(tweet.user.name)))
                db.commit()
                status_id.append(tweet.id)
		print tweet.id
        except tweepy.TweepError:
            print ' '


    for id in status_id:
        try:
            retweets = api.retweets(long(id))
            if len(retweets):
                for retweet in retweets:
                    sql1 = 'REPLACE INTO tweets_comments (status_id,comment_id,created_at,text,name,user_id) VALUES (%s,%s,%s,%s,%s,%s)'
                    cursor.execute(sql1, (
                        str(id), str(retweet.id), retweet.created_at, str(retweet.text), str(retweet.user.name),
                        str(retweet.user.id)))
                    db.commit()
        except tweepy.TweepError:
            print ' '
    time.sleep(43200)
