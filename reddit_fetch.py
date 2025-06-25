import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def fetch_posts(subreddit_name="conspiracy", limit=100):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):
        posts.append({
            "id": post.id,
            "title": post.title,
            "selftext": post.selftext,
            "author": str(post.author),
            "score": post.score,
            "num_comments": post.num_comments,
            "created_utc": post.created_utc,
            "permalink": f"https://www.reddit.com{post.permalink}"
        })

    return posts
