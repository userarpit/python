import json
from pprint import pprint

data = {
    "user": {"name": "John Doe", "age": 30, "city": "New York"},
}

data_tuple = ("Q", 2)

with open("../data/data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

data_str = json.dumps(data_tuple, indent=4)
pprint(data_str)

print(type(json.loads(data_str)))
pprint(json.loads(data_str))
