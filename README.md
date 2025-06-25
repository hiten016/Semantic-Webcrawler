# Reddit-Semantic-Crawler
This project crawls Reddit posts from a selected subreddit and performs semantic similarity analysis using a combination of Sentence-BERT for text embedding and FAISS for fast similarity search.

We use the PRAW API to fetch Reddit posts, encode them using the  Sentence-BERT model, and build a FAISS index to find and compare semantically similar posts efficiently. This helps in uncovering related discussions, coordinated content, or topic clustering within Reddit.
