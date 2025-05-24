# AI-Powered GitHub Repository Assistant

This project is a Python-based assistant designed to interact with GitHub repositories. It can clone repositories, parse code and markdown files, generate embeddings using HuggingFace's InstructorEmbedding, store embeddings in Chroma DB, and provide a Retrieval-Augmented Generation (RAG) system using LangChain with OpenRouter as the LLM provider.

## Features

- Clone or download GitHub repositories
- Parse code and markdown files
- Chunk content and generate embeddings
- Store embeddings in Chroma DB
- Retrieval-Augmented Generation (RAG) system with LangChain
- Command-line interface (CLI) for user interaction

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the CLI:
   ```bash
   python main.py
   ```

## Folder Structure

```
.
├── main.py                # Entry point for the CLI
├── modules/               # Contains modular components
│   ├── github_handler.py # Handles GitHub repo cloning and downloading
│   ├── parser.py         # Parses code and markdown files
│   ├── embedder.py       # Generates embeddings using HuggingFace
│   ├── db_handler.py     # Manages Chroma DB storage
│   └── rag_system.py     # Implements the RAG system with LangChain
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
```

## Requirements

- Python 3.8+
- pip

## License

This project is licensed under the MIT License.