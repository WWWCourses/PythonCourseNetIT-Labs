import socket

PORT = 5050
SERVER_NAME = 'x1c5'
SERVER_IP = socket.gethostbyname(SERVER_NAME)
CLIENT_NAME = socket.gethostname()
CLIENT_IP = socket.gethostbyname(CLIENT_NAME)
ENCODING="utf-8"

BUF_SIZE = 1024

def send_message(msg):
	s.send(msg.encode(ENCODING))

# define an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the server given with (SERVER_IP, PORT) tupple:
s.connect((SERVER_IP, PORT))
print(f'Client is connected to {(SERVER_IP, PORT)} ')
print(f'Client IP: {CLIENT_IP}, NAME: {CLIENT_NAME} ')

while True:
	msg = input("Enter message:")

	if(msg == ""):
		break;
	else:
		send_message(msg)


