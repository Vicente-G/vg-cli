import os
from tools import getch

# Git shortcut of Add
def git_add(*args, skip = False):
    os.system("git status | head -n 1")
    s = "s" if len(args) == 1 else ""
    advertance = f"continue to add {len(args)} file{s}? (y/n): "
    if "." in args:
        advertance = f"continue to add ALL files? (y/n): "
        args = ["."]
    if not skip:
        print(advertance)
    if skip or getch().lower() == "y":
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
        if not skip:
            print(f"Clonning into {cwd}, continue? (y/n) ")
        if skip or getch() == "y":
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
        os.system("printf \"At \"")
        check = os.system("git remote | grep -w origin")
        if check != 0:
            os.system(f"git remote add origin {url}")
            return 0
        os.system("printf \"The current url is: \"")
        os.system("git remote get-url origin")
        if not skip:
            print(f"Continue changing to {url}? (y/n) ")
        if skip or getch() == "y":
            os.system(f"git remote set-url origin {url}")
        return 0
    elif os.path.exists('./.git'):
        os.system("git rev-parse --abbrev-ref HEAD > .git/p-branch.txt")
        branch = ""
        with open(".git/p-branch.txt", "r") as file:
            branch = file.read().replace("\n", "").replace("\r", "")
        os.system("rm .git/p-branch.txt")
        os.system(f"git push -u origin {branch}")
        return 0
    print("vg: error: not in a git repository, neither a url provided")
    return 1
