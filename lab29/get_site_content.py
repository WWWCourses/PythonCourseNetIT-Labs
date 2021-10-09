import requests

urls_to_visit = [
	"https://www.autokelly.bg/"
]

url = urls_to_visit[0]
output = "./data/autokelly.bg.html"

# we can send headers:
headers = {
	"Cookie": "PHPSESSID=dtluk7o3u4eu7ia0or8nop22r2",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

# make GET request. Returns a Response object
r = requests.get(url, headers=headers, verify=False)
requests.get()

# explicitly specify encoding
r.encoding = "utf-8"

# get row HTML text:
content = r.text

with open(output, "w") as fh:
	fh.write(content)

