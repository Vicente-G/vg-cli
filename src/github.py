from config import load_config
from tools import rlinput
from os import system

def gh_make_pr(skip = False):
    config = load_config()
    title = rlinput("Set title? (last commit) ")
    if title == "":
        with open(".git/COMMIT_EDITMSG", "r") as file:
            title = file.read().replace("\n", "").replace("\r", "")
    body_questions = config["pr-format"]
    body = ""
    for question in body_questions:
        body += "## " + question["title"] + "\n\n"
        body += rlinput(question["title"] + " ", question["default"]) + "\n\n"
    with open(".git/pr-body.md", "w") as file:
        file.write(body)
    system(f"gh pr create --title \"{title}\" --body-file .git/pr-body.md")
    system("rm .git/pr-body.md")
