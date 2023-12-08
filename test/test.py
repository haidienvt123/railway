import requests

files = {'file': open('./test.txt', 'rb')}
resp = requests.post("http://127.0.0.1:5000", files=files)

print(files)

print(resp.json()) 