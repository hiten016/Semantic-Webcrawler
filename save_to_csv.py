import pandas as pd

def save_posts(posts, filename="reddit_posts.csv"):
    df = pd.DataFrame(posts)
    df.to_csv(filename, index=False)
    print(f"Saved {len(posts)} posts to {filename}")

