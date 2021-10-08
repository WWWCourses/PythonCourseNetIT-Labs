import socket
import threading

PORT = 5050
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
BUF_SIZE = 1024
ENCODING = "utf-8"


def process_request(request):
	# ------------------------------- parse request ------------------------------ #
	headers = request.split('\n')
	first_line=headers[0].split()
	method=first_line[0]
	path=first_line[1]

	# ------------------------------- make response ------------------------------ #
	if method=="GET":
		# generate status line and headers
		status_line = "HTTP/1.1 200 OK\n"
		headers = "Server: My Python Server\n"

		# generate body
		body="Hello"
		# TASK: return the file requested in path as body
		print(f'Task: Read file: {path} and send it as body')

		response = status_line + headers + "\n" + body


	if method=="POST":
		pass
		# get data from request body
		# do something with data
		# return response

	return response


# ----------------------- init server listening socket ----------------------- #
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))
s.listen()

print(f"Server is listening on {SERVER_IP}:{PORT}")

# ---------------------------- listen for clients ---------------------------- #
while True:
	(conn, addr) = s.accept()

	# ----------------------- get client's request message: ---------------------- #
	msg_bytes = conn.recv(BUF_SIZE)
	request = msg_bytes.decode(ENCODING)
	print(f'request: {request} ')

	# ----------------------- return HTTP formatted response ---------------------- #
	response = process_request(request)
	conn.send(response.encode(ENCODING))

	# ------------------------- close client's connection ------------------------ #
	conn.close()



