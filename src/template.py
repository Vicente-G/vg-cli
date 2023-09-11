import os
from config import load_config
from license import MIT_LICENSE
from tools import getch, askyn

def gh_template_use(name, sources):
    templates = " ".join([source["display"] for source in sources.values()])
    print(f"Use template? ({templates}) ")
    template = getch()
    if template in sources:
        os.system(f"git clone {sources[template]['url']} {name.lower()}")
        return sources[template]
    print("Template not found, starting an empty project")
    os.system(f"mkdir {name.lower()}")

def change_in_file(filename, *args):
    content = []
    with open(filename, "r") as file:
        content = file.readlines()
        for old, new in args:
            content = [line.replace(old, new) for line in content]
    with open(filename, "w") as file:
        for line in content:
            file.write(line)

def gh_setup_template(name, owner, template):
    cwd = os.path.realpath('.')
    if template is None:
        with open(f"{cwd}/LICENSE", "w") as file:
            file.write(MIT_LICENSE % (owner))
        with open(f"{cwd}/README.md", "w") as file:
            file.write(f"# {name}\n")
        return
    owner_and_name = template["url"].split(":")[1][:-4]
    just_name = owner_and_name.split("/")[1]
    config_file = template["config-file"]
    change_in_file(
        f"{cwd}/README.md",
        (owner_and_name, f"{owner}/{name}"),
        (just_name.lower(), name.lower()),
        (just_name, name)
    )
    change_in_file(
        f"{cwd}/LICENSE",
        (owner_and_name.split("/")[0], owner)
    )
    change_in_file(
        f"{cwd}/{config_file}",
        (just_name.lower(), name.lower())
    )

def gh_init(skip = False):
    config = load_config()
    user, cwd = config["username"], os.path.realpath('.')
    if askyn(f"Starting project in {cwd}, continue?", skip):
        return 0
    name = input("What is the project name? ")
    template_used = gh_template_use(name, config["templates"])
    os.chdir(name.lower())
    if template_used is not None:
        os.system("rm -rf .git")
    os.system("git init")
    owner = input(f"Who owns this project? ({user}) ")
    if owner == "":
        owner = user
    if os.system(f"gh repo create --private {owner}/{name}") != 0:
        return 1
    gh_setup_template(name, owner, template_used)
    url = f"git@github.com:{owner}/{name}.git"
    os.system(f"git remote add origin {url}")
    if template_used is not None:
        os.system("git add .")
        os.system("git commit -S -m \"First Commit\"")
        os.system("git push -u origin main")
        os.system("git checkout -b feat/v1")
