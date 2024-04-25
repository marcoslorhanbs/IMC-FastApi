import requests

req = requests.get("http://127.0.0.1:8000/imc/?peso=66.2&altura=1.66")
print(req.json())
