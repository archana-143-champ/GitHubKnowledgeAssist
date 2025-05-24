import os
from git import Repo

def clone_repo(repo_url):
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    repo_path = os.path.join(os.getcwd(), repo_name)
    if not os.path.exists(repo_path):
        print(f"Cloning repository {repo_url}...")
        Repo.clone_from(repo_url, repo_path)
    else:
        print(f"Repository {repo_name} already exists at {repo_path}.")
    return repo_path