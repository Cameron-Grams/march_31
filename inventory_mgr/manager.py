import requests

url = "http://localhost:8000/users/"

body = {
    "email": "a44@b",
    "password": "44string"
     }


resp = requests.post(url, json=body)

print(resp.text)
