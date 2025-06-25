from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

def embed_posts(posts):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = [post["title"] + " " + post["selftext"] for post in posts]
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings, texts

def build_faiss_index(embeddings):
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    return index

