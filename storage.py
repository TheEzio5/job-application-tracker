import json
FILE_NAME = "applications.json"

def load_data():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
        data = json.load(json_file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE_NAME,"w") as file:
        json.dump(data,file,indent=4)
