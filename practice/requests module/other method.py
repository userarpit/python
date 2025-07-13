import requests

response = requests.get("https://httpbin.org/get")
print(response.text)

response = requests.post("https://httpbin.org/post", data={"key": "value"})
print(response.text)

response = requests.head("https://httpbin.org/get")
print(response.headers['Content-Type'])