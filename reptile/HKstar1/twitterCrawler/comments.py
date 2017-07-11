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
f=open(r'C:\Users\Administrator\Desktop\tweets_id.txt')

api = tweepy.API(auth,proxy="127.0.0.1:1080",wait_on_rate_limit=True)

# db = pymysql.connect(host="202.110.49.146", user="root", passwd="Sz@860213", db="hkstar", charset="utf8")
db = pymysql.connect(host="192.168.1.20", user="root", passwd="root", db="hkstar", charset="utf8")

cursor = db.cursor()
# ids=f.readlines()
# i=0
while 1:
    id=f.readline()
    time.sleep(1)
    print id
    retweets = api.retweets(long(id))
    if len(retweets):
        for retweet in retweets:
            sql='INSERT IGNORE INTO tweets_comments (status_id,comment_id,created_at,text,name,user_id) VALUES (%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (str(id), str(retweet.id),retweet.created_at,str(retweet.text),str(retweet.user.name),str(retweet.user.id)))
            db.commit()


