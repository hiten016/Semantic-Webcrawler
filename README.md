Reddit-Semantic-Crawler-using-BERT-FAISS
This project crawls Reddit posts from a chosen subreddit and performs semantic analysis to find similar discussions using a combination of Sentence-BERT for embedding generation and FAISS for fast similarity search.

We use the PRAW API to extract Reddit data, encode each post's text using a Sentence-BERT model (all-MiniLM-L6-v2), and build a FAISS index to enable efficient nearest-neighbor searches for semantically similar posts. This can help detect coordinated narratives, repetitive propaganda, or simply related conversations.
