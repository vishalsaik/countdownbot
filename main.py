import tweepy
import os
from datetime import datetime
import pytz  # For timezone support

# Fetch secrets from environment variables
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Set IST timezone
ist = pytz.timezone('Asia/Kolkata')

# Get current datetime in IST and convert to date
now = datetime.now(pytz.UTC)  # Start with UTC time
ist_now = now.astimezone(ist)  # Convert to IST
today = ist_now.date()

# Debug output
print(f"UTC Time: {now}")
print(f"IST Time: {ist_now}")
print(f"Today’s Date (IST): {today}")

# Target release date
release_date = datetime(2026, 3, 26).date()

# Calculate days left
days_left = (release_date - today).days

# Create tweet with just the number
tweet_text = str(days_left)

# Create tweet
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

try:
    response = client.create_tweet(text=tweet_text)
    print(f"Tweeted! ID: {response.data['id']}")
    with open('main.py.out', 'w') as f:
        f.write(f"Tweeted! ID: {response.data['id']}")
except Exception as e:
    error = f"Error: {e}"
    print(error)
    with open('main.py.out', 'w') as f:
        f.write(error)