import tweepy
import facebook
import random
import string

# Function to generate random API keys for testing
def generate_random_key(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Twitter setup
def fetch_twitter_data():
    consumer_key = generate_random_key()  # Random consumer key
    consumer_secret = generate_random_key()  # Random consumer secret
    access_token = generate_random_key()  # Random access token
    access_token_secret = generate_random_key()  # Random access token secret
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.search_tweets(q='Python', count=10)
    return [{'text': tweet.text} for tweet in tweets]

# Facebook setup
def fetch_facebook_data():
    access_token = generate_random_key()  # Random access token for Facebook
    graph = facebook.GraphAPI(access_token)

    posts = graph.get_connections(id='me', connection_name='posts')
    return [{'text': post['message']} for post in posts['data'] if 'message' in post]

# Test fetch
twitter_data = fetch_twitter_data()
facebook_data = fetch_facebook_data()

print(twitter_data)
print(facebook_data)
