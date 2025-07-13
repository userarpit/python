import json

with open("../data/mini_frieda.json",mode="r",encoding="utf-8") as json_file:
    json_data = json_file.read()
    data = json.loads(json_data)

print(data)
