#TP Final MAM Juan Patricio Di Bacco

#We will need to import several libs for this project:

import os
import json
from twitter import Api
import time
import threading
from threading import Thread
from functools import partial

#Since we are going to be streaming tweets we will need to set up a Twitter App. Here's my consumer keys and access token keys from twitter app:
CONSUMER_KEY = 'aKgzBXWNPYr2DX1eJ0PFzwiwO'
CONSUMER_SECRET = 'SS5iZ51zMfUytL1rwdKnxz4Gxdej5q75gxf6QvvlIfmeTV76Hj'
ACCESS_TOKEN = '751666722592198656-SE6Tii2c7LnTiTWttMTGUVHkQzhmBHT'
ACCESS_TOKEN_SECRET = 'dwJ73N7ug7LuJmvzIWK6L0X9TW7vOlBMyIec7s0OyYnhV'
#We can choose one or several searchs such as users: @twitteruser or hashtags: #myhashtag. Example: USERS_AND_HASHTAG = ['@user','#hashtag'], in this case scenario we are going to limit the search for one hashtag:
HASHTAG = ['#Argentina']
#We call the api from twitter and connect:
api = Api(CONSUMER_KEY,
          CONSUMER_SECRET,
          ACCESS_TOKEN,
          ACCESS_TOKEN_SECRET)
#variable object to set the tweets
tweets = []
#Function for gettings tweets and saving them into a JSON file:
def getTweets(limit):
        count_tweets = limit
        with open('mam2.json', 'a') as data:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
            for line in api.GetStreamFilter(track=HASHTAG):
                data.write(json.dumps(line))
                data.write('\n')
                print count_tweets, '# of tweets'
                count_tweets -=1
                if count_tweets == 0:
                    print 'limit of tweets reached'
                    time.sleep(5)
                    count_tweets = limit


#This is where we call both functions to work together:
def main():
    limit = 2
    #we can also limit one of the functions, but in this project we will keep it free:
    #partial1 = partial(getTweets, r=88)
    #t1 = Thread(target=partial1)
    t1 = Thread(target=getTweets(limit))
    t1.start()
if __name__=='__main__':
    main()
