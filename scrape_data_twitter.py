#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import csv
import json
import wget


# Twitter API credentials

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the maximum number of tweets that you want to be extracted.

maximum_number_of_tweets_to_be_extracted = int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for
print(maximum_number_of_tweets_to_be_extracted)
hashtag = input('Enter the hashtag you want to scrape- ')


all_tweets = tweepy.Cursor(api.search, q='#' + hashtag,
                           rpp=100).items(maximum_number_of_tweets_to_be_extracted)

image_files = set()
for tweet in all_tweets:
    media = tweet.entities.get('media', [])
    if len(media) > 0:
        image_files.add(media[0]['media_url'])
        #print("Name:", tweet.author.name.encode('utf8'))
        #print("Screen-name:", tweet.author.screen_name.encode('utf8'))
        print("Tweet created:", tweet.created_at)
        #print("Tweet:", tweet.text.encode('utf8'))
        #print("Retweeted:", tweet.retweeted)
        #print("Favourited:", tweet.favorited)
        print("Location:", tweet.user.location.encode('utf8'))
        print("Time-zone:", tweet.user.time_zone)
        #print("Geo:", tweet.geo)
        print()

print ('Downloading ' + str(len(image_files)) + ' images.....')
for image_file in image_files:
    wget.download(image_file)

