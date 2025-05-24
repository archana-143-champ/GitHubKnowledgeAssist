import os

def parse_files(repo_path):
    """Parses code and markdown files in the repository."""
    parsed_content = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(('.py', '.md')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    parsed_content.append(f.read())
    return parsed_content