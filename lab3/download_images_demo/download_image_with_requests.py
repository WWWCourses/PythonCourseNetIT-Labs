import requests

url = "https://unsplash.com/photos/zb02pCHXmeo/download?force=true"

# splitted = url.split('/')
# print(splitted)

# get image name from URL (the part: 'zb02pCHXmeo')
file_name = url.split('/')[4]+".jpg"

# get image bytes
print(f"Start downloading {url}")
response = requests.get(url)

# write image to file
with open(file_name, 'wb') as fh:
  fh.write(response.content)
  print(f"File saved to {file_name}")