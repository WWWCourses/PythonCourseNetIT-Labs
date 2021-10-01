import socket

PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())
BUFF_SIZE=1024
FORMAT="utf8"
DISCONNECT_MESSAGE = "exit"


def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	connected = True

	while connected:
		msg_length = conn.recv(BUFF_SIZE)

		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f"[{addr}] says: {msg}")
			conn.send("Msg received".encode(FORMAT))

	conn.close()

# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tell the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the host
s.bind((SERVER_IP, PORT))

s.listen()
print(f"Server is listening on {SERVER_IP}:{PORT}")


while True:
  conn, addr = s.accept()
  # better to do with threading
  handle_client(conn, addr)

  print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")