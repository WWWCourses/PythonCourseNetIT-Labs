import socket

PORT = 5050
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
BUF_SIZE = 1024
ENCODING="utf-8"


def receive_message(s):
	msg_bytes = s.recv(BUF_SIZE)
	print(f'Received: ', msg_bytes.decode(ENCODING))

# define an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse port:

# now connect to the server given with (SERVER_IP, PORT) tupple:
s.bind((SERVER_IP, PORT))
s.listen()

print(f"Server is listening on {SERVER_IP}:{PORT}. Name: {SERVER_NAME}")


while True:
	(conn, addr) = s.accept()
	print(conn, addr)

	# receive_message(conn)

	msg = conn.recv(BUF_SIZE)
	print(msg)
