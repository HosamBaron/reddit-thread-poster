
import praw

# Reddit API credentials
reddit = praw.Reddit(
    client_id='R6RzOd5oHlgTnAxrdt4FrA',
    client_secret='FST0qJX51u2KY9NCvWCG4mxQw4s8Jw',
    username='Guilty_Floor9214',
    password='NoorAlden1',
    user_agent='web:com.example.myredditapp:v1.0 (by /u/Guilty_Floor9214)'
)

subreddit = reddit.subreddit('AllHayganeen')

print("Available flairs:")
for flair in subreddit.flair.link_templates:
    print(f"ID: {flair['id']}, Text: {flair['text']}")

