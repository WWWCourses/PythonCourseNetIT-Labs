import socket

PORT = 5050
SERVER_IP = socket.gethostbyname(socket.gethostname())
BUFF_SIZE=1024
FORMAT="utf8"
DISCONNECT_MESSAGE = "exit"

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)

  # pad message to be send to BUFF_SIZE
  send_length += b' ' * (BUFF_SIZE - len(send_length))

  s.send(send_length)
  s.send(message)
  print(s.recv(BUFF_SIZE).decode(FORMAT))


# create an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'Client is connected to {(SERVER_IP, PORT)} ')

# now connect to the server given with (SERVER_IP, PORT) tupple:
s.connect((SERVER_IP, PORT))

# send some messages:
while True:
  msg = input("Enter a message:")
  if msg == '':
    send(DISCONNECT_MESSAGE)
  else:
    send(msg)