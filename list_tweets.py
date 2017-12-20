import tweepy

from config import consumer_key, consumer_secret, access_key, access_secret


def list_all_tweets(name):
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets
    new_tweets = api.user_timeline(name=name, count=200, include_rts=True)
    for status in new_tweets:

        print(status.text)
        alltweets.append(status.text)
    return alltweets
if __name__ == '__main__':
    # pass in the username of the account you want to download
    list_all_tweets("abiralsambhu")