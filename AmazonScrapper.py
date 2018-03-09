#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from tweepy import *
import tweepy
import time

consumer_key = 'cujbknKffQfOrZNwq5NoqPfNP'
consumer_secret = 'vKAYadwi77IMveroNSqGmEDz0hVoNEn6LeIrelew6ya29mRjLs'
access_token = '2830219376-Sjk8YvZtWSdxZxdZyy5t91wtwIHd2FYpAadWnmJ'
access_token_secret = 'RAhkc6SY72fkolUfAjCnFO5yfKcOkqlxtjluh0Ece9Xqj'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
trends1 = api.trends_place(23424975)

open('datalog_tweets.txt', 'w')

tweets = []

for location in trends1:
    for trend in location["trends"]:
        # print ("%s" % trend["name"])
        f =  open('datalog_tweets.txt', 'a', encoding="utf8")
        f.write("%s\n" % trend["name"].replace("#", ''))
        tweets.append("%s" % trend["name"].replace("#", '').replace(" ", "+"))

# print(tweets)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
links = []
for query in tweets:
    time.sleep(20)
    print(query)
    r = requests.get('https://www.google.com/search?q=site:amazon.com+{}&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw'.format(query), headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.find_all('h3', attrs={'class' : 'r'}, limit=1):
        links.append(item.a['href'][7:])

print(links)

for link in links:
    link.replace("?q=site:", "https://")

for link in links:
    print(link)