import tweepy
import os
from config import consumer_key, consumer_secret,access_key, access_secret
#Add your key details by obtaining from app.twitter.com
#
#add in separate `config.py` file or add here defining variable as used here
#
def tweet(status):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status(status)


if __name__== "__main__":
    status = input("Enter tweet: ")
    tweet(status=status)
