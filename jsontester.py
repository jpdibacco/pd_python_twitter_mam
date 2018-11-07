#TP Final MAM Juan Patricio Di Bacco

#We will need to import several libs for this project:

import os
import json
import time
import threading
from threading import Thread
from functools import partial
import numpy as np

#variable object to set the tweets
tweets = []
worda = []
wordb = []
text = []
amount_of_words = []
#Function for reading one tweeet of the JSON file and converting the letters into numbers:
def reader(value):
    count_tweet = 0
    for line in open('/Users/jpdibacco/MAM/TP_Final/mam.json'):
        try:
            tweets.append(json.loads(line))
            #count_tweet += 1
            #if count_tweet > 1:
                #tweet = tweets[2]
                #break
        except:
            pass
#In order to read the tweets in an indent format we can uncomment the code bellow:
#print json.dumps(tweets, indent=4)
#This is where we start counting words from tweets:
    #tweetsb = tweets[value]
    global amount_of_words
    for tweet in tweets:
        #text = tweet.get('text')
        text = [tweet['text'] for tweet in tweets]
    #print text[value], 'text from tweet'
    amount_of_words = text[value].split(' ')
        #print json.dumps(tweets, indent=4)
    #print len(amount_of_words),'--amount of words'
    a = len(amount_of_words)
    #for word in amount_of_words:
        #worda = len(word)
        #wordb.append(worda)
    #return total value of each word:
    print a
    #return a
        #return wordb
def readeachword(value):
    for word in amount_of_words:
        worda = len(word)
        wordb.append(worda)
    print wordb, 'total words'
    print wordb[value]
    #return wordb[value]
reader(0)
readeachword(0)