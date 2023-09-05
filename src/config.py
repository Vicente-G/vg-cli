import json

def load_config():
    config = {}
    with open("/usr/local/lib/vg/config.json", "r") as file:
        config = json.load(file)
    return config
