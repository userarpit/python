import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout


with requests.Session() as session:

    try:
        response = session.get(
            "https://httpbin.org/basic-auth/user/passwd",
            auth=HTTPBasicAuth("user", "passwd"),
            timeout=(1, 1),
        )
        print(response.status_code)
        print(response.text)
        print(response.request.headers["Authorization"])
        
        response = session.get(
            "https://httpbin.org/basic-auth/user/passwd",
            auth=HTTPBasicAuth("user", "passwd"),
            timeout=(1, 1),
        )

    except Timeout:
        print("Timeout ")
