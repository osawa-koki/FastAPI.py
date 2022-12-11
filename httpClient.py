import requests
import json

domain = "localhost:8000"
path = ""

payload = {
    "number": 25,
    "name": "ピカチュウ",
    "type1": "でんき",
    "type2": "なし"
}

response = requests.post("http://{}/{}".format(domain, path), data=json.dumps(payload))

print(response.text)
