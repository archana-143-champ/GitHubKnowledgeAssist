import argparse
from modules.github_handler import clone_repo
from modules.rag_system import ask_question

def main():
    parser = argparse.ArgumentParser(description="AI-Powered GitHub Repository Assistant")
    parser.add_argument("repo_url", help="URL of the GitHub repository to clone")
    parser.add_argument("question", help="Question to ask about the repository")
    args = parser.parse_args()

    # Clone the repository
    repo_path = clone_repo(args.repo_url)

    # Ask a question using the RAG system
    answer = ask_question(repo_path, args.question)
    print("Answer:", answer)

if __name__ == "__main__":
    main()