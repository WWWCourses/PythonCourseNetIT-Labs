import requests
import concurrent.futures
import os
import time


def download_file(url):
	file_name=url.split('/')[4]+'.jpg'

	full_file_name = os.path.join(download_path,file_name)

	# get image bytes
	print(f"Start downloading {url}")
	response = requests.get(url, allow_redirects=True)

	# write image to file
	with open(full_file_name, 'wb') as fh:
		fh.write(response.content)
		print(f"File saved to {full_file_name}")

urls = [
	"https://unsplash.com/photos/CTflmHHVrBM/download?force=true",
	"https://unsplash.com/photos/pWV8HjvHzk8/download?force=true",
	"https://unsplash.com/photos/1jn_3WBp60I/download?force=true",
	"https://unsplash.com/photos/8E5HawfqCMM/download?force=true",
	"https://unsplash.com/photos/yTOkMc2q01o/download?force=true"
]

download_path = os.path.join(os.getcwd(),"downloaded_images")

if __name__ == "__main__":
	start= time.perf_counter()

	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(download_file, urls)


	end = time.perf_counter()

	print(f"Procesing time:  {end-start}")
