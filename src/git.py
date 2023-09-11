import os
from tools import getch, askyn, get_one_line, srun

# Git shortcut of Add
def git_add(*args, skip = False):
    os.system("git status | head -n 1")
    if len(args) == 0:
        print("vg: error: no files provided")
        return 1
    s = "s" if len(args) != 1 else ""
    advertance = f"continue to add {len(args)} file{s}?"
    if "." in args:
        advertance = f"continue to add ALL files?"
        args = ["."]
    if askyn(advertance, skip):
        files = " ".join(args)
        os.system(f"git add {files}")
        print("files added successfully!")
    return 0

# Git shortcut of Branch
def git_branch(name, skip = False):
    os.system(f"git branch -M {name}")
    return 0

# Git shortcut of Commit
def git_commit(skip = False):
    options = {
        "t": "feat: ",
        "x": "fix: ",
        "d": "docs: ",
        "s": "style: ",
        "r": "refactor: ",
        "c": "chore: ",
        "n": ""
    }
    print("Commit Type? (fea[T] fi[X] [D]ocs [S]tyle [R]efactor [C]hore [N]one): ")
    if (c := getch()) not in options:
        print("vg: error: commit type not yet implemented")
        return 1
    if c != "n":
        scope = input("Commit scope: (optional) ")
        if scope != "":
            options[c] = options[c].replace(":", f"({scope}):")
    message = input("Commit message: ")
    if c != "n":
        message = message.lower()
    commit = f"{options[c]}{message}"
    os.system(f"git commit -S -m \"{commit}\"")
    return 0

# Git shortcut of Clone/Pull
def git_download(url = None, skip = False):
    if url is not None:
        cwd = os.path.realpath('.')
        if askyn(f"Clonning into {cwd}, continue?", skip):
            os.system(f"git clone {url}")
        return 0
    elif os.path.exists('./.git'):
        os.system("git pull")
        return 0
    print("vg: error: not in a git repository, neither a url provided")
    return 1

# Git shortcut of Remote/Push
def git_upload(url = None, skip = False):
    if url is not None:
        if srun("git remote | grep -w origin") != 0:
            os.system(f"git remote add origin {url}")
            return 0
        os.system("printf \"The current url is: \"")
        os.system("git remote get-url origin")
        if askyn(f"Continue changing to {url}?", skip):
            os.system(f"git remote set-url origin {url}")
        return 0
    elif os.path.exists('./.git'):
        os.system("git rev-parse --abbrev-ref HEAD > .git/p-branch.txt")
        branch = get_one_line(".git/p-branch.txt")
        os.system(f"git push -u origin {branch}")
        return 0
    print("vg: error: not in a git repository, neither a url provided")
    return 1
