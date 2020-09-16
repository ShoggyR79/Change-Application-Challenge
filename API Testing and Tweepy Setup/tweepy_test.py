import tweepy
import random
import re
###


kanye_id = 614754689
elon_id = 44196397

kanye_tweets = []
elon_tweets = []


# standard tweepy api setup procedure
consumer_key = "J1vCFHVRQsxUDwUrylGfkdiPO"
consumer_secret = "Xi0ZswCiZvTgYHYCyo7ucGK8qytLpLEmfxQzc2BLI6UKSLugAc"

access_token = "794730854354448384-g7aORg91y3e6m6jkLJwFqpVyrUNkpXE"
access_token_secret = "9O4MJnJZRJ4fTX8k2zYjG0CHUwpA3KFDeEoNXYkcThofI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token( access_token, access_token_secret)

api = tweepy.API(auth)


# gets x amount of tweets from "user_id"
for status in tweepy.Cursor(api.user_timeline,
                            user_id=kanye_id,
                            tweet_mode="extended",
                            include_rts=False,
                            exclude_replies=True
                            ).items(20):

    # deletes urls from tweet
    filtered_tweet = re.sub(r"http\S+", "", status.full_text)

    # if tweet still contain stuff after URL is deleted, it is added to stash
    if filtered_tweet:
        kanye_tweets.append(status)

# picks a random tweet Status object from inventory of statuses
tweet_picked = random.choice(kanye_tweets)

# filters out the url again (the filtering done above only serve as a checking mechanism)

filtered_tweet = re.sub(r"http\S+", "", tweet_picked.full_text)

# Prints that tweet.
print(filtered_tweet + "\ntweeted at " + str(tweet_picked.created_at))



