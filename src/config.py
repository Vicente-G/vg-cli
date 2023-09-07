import json
import os

CONFIG_FILE = "/usr/local/lib/vg/config.json"

def load_config():
    config = {}
    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)
    return config

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def add_template(skip = False):
    config = load_config()
    user, temps = config["username"], config["templates"]
    name = input("Template name: (no spaces) ").lower().split(" ")[0]
    keys = list(filter(lambda c: c not in temps, [char for char in name]))
    if len(keys) == 0:
        print("vg: error: invalid template name, please try again")
        return 1
    display = "(" + "/".join(keys) + ")"
    while (key := input(f"Choose a key: {display} ")) not in keys:
        print("Choose a key within the brackets")
    name = name[:name.find(key)] + key.upper() + name[name.find(key)+1:]
    cfile = input("Config file: (package.json) ") or "package.json"
    owner = input(f"Template owner: ({user}) ") or user
    repo = input("Template repository name: ")
    url = f"http://github.com/{owner}/{repo}/blob/main/{cfile}"
    flags = "--head --silent --fail"
    check = os.system(f"curl {flags} {url} &> /dev/null")
    if check != 0:
        print("vg: error: repo doesn't respond, please try again")
        return 1
    config["templates"][key] = {
        "display": name.replace(key.upper(), f"[{key.upper()}]"),
        "config-file": cfile,
        "url": f"git@github.com:{owner}/{repo}.git"
    }
    save_config(config)
    print(f"Template {name} added successfully!")
    return 0
