from langchain.chains import RetrievalQA
from langchain.llms import OpenRouter
from modules.parser import parse_files
from modules.embedder import generate_embeddings
from modules.db_handler import store_embeddings

def ask_question(repo_path, question):
    """Sets up a RAG system and answers a question about the repository."""
    # Parse files
    content = parse_files(repo_path)

    # Generate embeddings
    embeddings = generate_embeddings(content)

    # Store embeddings in Chroma DB
    collection = store_embeddings(embeddings)

    # Set up RAG system
    retriever = collection.as_retriever()
    llm = OpenRouter(api_key="your-api-key")
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)

    # Get answer
    return qa_chain.run(question)