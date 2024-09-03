import tweepy
import facebook

# Twitter setup
def fetch_twitter_data():
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.search_tweets(q='Python', count=10)
    return [{'text': tweet.text} for tweet in tweets]

# Facebook setup
def fetch_facebook_data():
    access_token = 'your_access_token'
    graph = facebook.GraphAPI(access_token)

    posts = graph.get_connections(id='me', connection_name='posts')
    return [{'text': post['message']} for post in posts['data'] if 'message' in post]
