import tweepy
from datetime import datetime
import os

# Fetch secrets from environment variables
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Check if any key is missing
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    raise ValueError("Missing one or more API credentials in environment variables.")

MOVIE_HANDLE = '@YourMovieCD'  # Change to your movie's handle or name
RELEASE_DATE = datetime(2025, 10, 15)  # Example: October 15, 2025 - adjust this!

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Force fresh date calculation
today = datetime.now()
print(f"Current date and time: {today}")  # Debug output
days_left = (RELEASE_DATE - today).days

if days_left > 0:
    try:
        # Format tweet to match "PEDDI DAYS TO GO 180" look
        tweet_text = f"{MOVIE_HANDLE.replace('@', '').upper()} DAYS TO GO  {days_left}"
        response = client.create_tweet(text=tweet_text)
        output = f"Tweeted! ID: {response.data['id']}"
        print(output)
        with open('main.py.out', 'w') as f:
            f.write(output)
    except tweepy.Forbidden as e:
        error = f"Forbidden error: {e}"
        print(error)
        with open('main.py.out', 'w') as f:
            f.write(error)
    except Exception as e:
        error = f"Other error: {e}"
        print(error)
        with open('main.py.out', 'w') as f:
            f.write(error)
else:
    output = "Movie released—no tweet needed."
    print(output)
    with open('main.py.out', 'w') as f:
        f.write(output)