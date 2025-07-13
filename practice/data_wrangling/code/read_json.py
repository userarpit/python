import json

with open("../data/data.json") as json_file:
    json_data = json_file.read()
    data = json.loads(json_data)

    for item in data:
        print(item)
