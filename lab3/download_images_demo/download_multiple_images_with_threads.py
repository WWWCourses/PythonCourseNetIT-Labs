import requests
import threading
import os
import time

def download_image(url):
	file_name = url.split('/')[4]+".jpg"

	full_file_name = f"{os.getcwd()}/downloaded_images/{file_name}"

	# get image bytes
	print(f"Start downloading {url}")
	response = requests.get(url)

	# write image to file
	with open(full_file_name, 'wb') as fh:
		fh.write(response.content)
		print(f"File saved to {file_name}")


urls = [
	"https://unsplash.com/photos/zb02pCHXmeo/download?force=true",
	"https://unsplash.com/photos/cZNlLog1WyQ/download?force=true"
]

download_path = "downloaded_images"


if __name__ == "__main__":
	# ---------------------------------------------------------------------------- #
	#                             consequent processing                            #
	# ---------------------------------------------------------------------------- #
	# start = time.perf_counter()

	# for url in urls:
	# 	download_image(url)

	# end = time.perf_counter()
	# print(f"Downloaded time: {end - start}")


	# ---------------------------------------------------------------------------- #
	#                          thread - based parallelism                          #
	# ---------------------------------------------------------------------------- #
	start = time.perf_counter()

	threads = []

	for url in urls:
		tr = threading.Thread(target=download_image,args=(url,))
		tr.start()
		threads.append(tr)


	# wait until all threads finish
	for tr in threads:
		tr.join()

	end = time.perf_counter()
	print(f"Downloaded time: {end - start}")