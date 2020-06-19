#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 08:57:45 2020

@author: johnaustin
"""

import GetOldTweets3 as got
import pandas as pd

# Grab 1000 tweets mentioning coronavirus
tweetCriteria = got.manager.TweetCriteria()\
                           .setQuerySearch('coronavirus OR covid')\
                           .setMaxTweets(10_000)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

# These are the attributes of a tweet returned by GetOldTweets3
attributes = [
    'id',
    'permalink',
    'username',
    'to',
    'text',
    'date',
    'retweets',
    'favorites',
    'mentions',
    'hashtags',
    'geo'
]

# Create list of tweets to later turn into pandas df
tweets_dict = []
for tweet in tweets:
    tweet_dict = {}
    for attr in attributes:
        tweet_dict[attr] = getattr(tweet, attr) 
    tweets_dict.append(tweet_dict)

# Export tweets as a .csv
pd.DataFrame(tweets_dict).to_csv('../data/tweets.csv', index=False)