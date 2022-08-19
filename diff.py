import os
github_repo = ''

def cloneCollection():
    os.system("git clone " + github_repo)
    
def diff(id1: str, commit1: str, id2:str, commit2: str):
    os.system(f"diff <(git show {commit1}~1:file.json | gron) <(git show {commit1}~1:file.json | gron)")