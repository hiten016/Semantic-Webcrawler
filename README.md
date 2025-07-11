🕸️ Reddit Semantic Crawler
A semantic crawler and analyzer for Reddit that uses Sentence-BERT and FAISS to discover similar or coordinated posts in a given subreddit. This tool is ideal for research, community monitoring, or content clustering on Reddit.

 Key Features
 Crawl posts from any public subreddit using PRAW
 Generate high-dimensional embeddings using Sentence-BERT
 Build and query FAISS index for fast semantic similarity search
 Analyze coordinated content or topic clusters in Reddit posts
 Modular design for easy integration into research or moderation pipelines

⚙ Tech Stack
Layer	Tools / Libraries
Reddit API	PRAW
Embeddings	Sentence-BERT (via sentence-transformers)
Vector DB	FAISS
Backend	Python, Pandas
Visualization	Matplotlib / Seaborn (optional)
