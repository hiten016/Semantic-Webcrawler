# run.py

from reddit_fetch import fetch_posts
from extract_semantics import embed_posts, build_faiss_index
from save_to_csv import save_posts

def main():
    print("\n[*] Fetching posts from Reddit...")
    posts = fetch_posts(subreddit_name="conspiracy", limit=100)
    
    print("[*] Saving posts to CSV...")
    save_posts(posts, filename="reddit_posts.csv")

    print("[*] Generating embeddings using Sentence-BERT...")
    embeddings, texts = embed_posts(posts)

    print("[*] Building FAISS index for similarity search...")
    index = build_faiss_index(embeddings)

    print("\n🔍 Top 5 similar posts to the first one:")
    print(f"\n🧵 Query: {texts[0]}\n")

    query_vector = embeddings[0].reshape(1, -1)
    _, indices = index.search(query_vector, 5)

    for i in indices[0][1:]:  # Skip self-match at index 0
        print(f"→ {texts[i]}\n")

if __name__ == "__main__":
    main()
