import chromadb

def store_embeddings(embeddings):
    """Stores embeddings in Chroma DB."""
    client = chromadb.Client()
    collection = client.get_or_create_collection('repo_embeddings')
    for idx, embedding in enumerate(embeddings):
        collection.add(embedding_id=str(idx), embedding=embedding)
    return collection