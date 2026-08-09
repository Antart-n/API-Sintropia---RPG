import json
import os

FILE = "bd.json"
def load(file=FILE):
    if not os.path.exists(FILE):
        return {}
    
    with open(file, "r", encoding="utf-8") as path:
        data = json.load(path)
    return data

def save(new_data, file=FILE):
    with open(FILE, "w", encoding="utf-8") as path:
        json.dump(new_data, path, ensure_ascii=False, indent=4)

