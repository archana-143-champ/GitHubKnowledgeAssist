from sentence_transformers import SentenceTransformer


def generate_embeddings(content):
    print('Generating embeddings for the content...')
    """Generates embeddings for the given content using SentenceTransformer."""
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = [model.encode(text) for text in content]
    return embeddings
