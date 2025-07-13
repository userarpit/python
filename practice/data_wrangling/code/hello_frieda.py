import json

# with open("../data/hello_frieda.json") as json_file:
#     json_data = json_file.read()
#     data = json.loads(json_data)

#     for item in data:
#         print(item)

dog_data = {
    "name": "Frieda",
    "isDog": True,
    "hobbies": ["eating", "sleeping", "barking"],
    "age": 8,
    "address": {"work": None, "home": ["Berlin", "Germany"]},
    "friends": [
        {"name": "Philipp", "hobbies": ["eating", "sleeping", "reading"]},
        {"name": "Mitch", "hobbies": ["running", "snacking"]},
    ],
}

with open(
    "../data/hello_frieda.json", mode="w", encoding="utf-8"
) as json_file:
    json.dump(dog_data, json_file, indent=4)
