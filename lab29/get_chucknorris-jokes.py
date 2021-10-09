import requests

url = "https://api.chucknorris.io/jokes/random"

r = requests.get(url)
text = r.text;
content = r.json()
print(content['value'])