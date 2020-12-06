import tweepy
import time

auth = tweepy.OAuthHandler("3QZeqwUlBuBH5bmbRL1DuTy8K", "offZmQxEb9uvd4OeVK9NCx7Pd82c9bSRVYWyAngMZ9Q934p294")

auth.set_access_token("1081562955328643073-NBhLxBnmgnkVUV02rSyvsd5AfbeRNW",
                      "5bmadkZTE5zVGsvgEGtAb4LFbwwuLqUJkQcSUIS1S7znC")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# for follower in tweepy.Cursor(api.followers).items():
# print(follower.name)

# checking my followers names

search = 'Python'
nrTweets = 100
'''
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()   #you can use tweet.retweet() for retweeting
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
'''
# following people with certain hashtags
for follower in tweepy.Cursor(api.search, q="#Trump").items(nrTweets):
    if follower.favorite():
        api.create_friendship(screen_name=follower.author.screen_name)
        print(follower)
