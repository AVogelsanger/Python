# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:08:50 2019

@author: 748418
"""

#Twitter Sentiment Analysis - Learn Python for Data Science #2

from textblob import TextBlob as tb
import tweepy
import numpy as np

consumer_key = 'SUA CONSUMER KEY'
consumer_secret = 'SUA CONSUMER SECRET'
access_token = 'SEU ACCESS TOKEN'
access_token_secret = 'SEU ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Variável que irá armazenar todos os Tweets com a palavra escolhida na função search da API
public_tweets = api.search('Pelé')

analysis = None

tweets = [] # Lista vazia para armazenar scores
for tweet in public_tweets:
    print(tweet.text)
    analysis = tb(tweet.text)
    polarity = analysis.sentiment.polarity
    tweets.append(polarity)
    print(polarity)
    
    
    print('MÉDIA DE SENTIMENTO: ' + str(np.mean(tweets)))
    
    
    
    
    