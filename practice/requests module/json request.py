import requests

response = requests.post("https://httpbin.org/post", json={"key": 12})
print(response.json()["json"])