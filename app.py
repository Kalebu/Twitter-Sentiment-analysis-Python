from tweepy import API,  OAuthHandler
from textblob import TextBlob
from API_KEYS import api_key, api_secret_key

def clean_tweets(tweet):
    tweet_words = str(tweet).split(' ')
    clean_words = [word for word in tweet_words if not word.startswith('#')]
    return ' '.join(clean_words)

def analyze(Topic):
    positive_tweets, negative_tweets = [], []
    authentication = OAuthHandler(api_key, api_secret_key)
    api = API(authentication)
    public_tweets = api.search(Topic, count=10)
    cleaned_tweets = [clean_tweets(tweet.text) for tweet in public_tweets]
    for tweet in cleaned_tweets:
        tweet_polarity = TextBlob(tweet).sentiment.polarity
        if tweet_polarity<0:
            negative_tweets.append(tweet)
            continue
        positive_tweets.append(tweet)
    return positive_tweets, negative_tweets


positive, negative = analyze('Magufuli')
print(positive , '\n\n', negative)
print(len(positive), ' VS  ', len(negative))