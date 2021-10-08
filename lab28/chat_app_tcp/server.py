import socket
import threading

PORT = 5050
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
BUF_SIZE = 1024
ENCODING = "utf-8"


def receive_message(s):
    while True:
        client_port = s.getpeername()[1]
        msg_bytes = s.recv(BUF_SIZE)
        message = msg_bytes.decode(ENCODING)

        # TASK: do not print empty messages
        print(f'msg_bytes: {msg_bytes}')
        if msg_bytes == b'':
            print(f'Client ({client_port}) is dead')
            clients.remove(s)
            exit(0)

        print(f'Received: {message} ')

        # SENDING MESSAGE TO ALL CLIENTS IN A LIST, except current one:
        for client in clients:
            if client != s:
                client.send(f'{client_port}:{message}'.encode(ENCODING))



# define an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reuse port:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# set server to listen for incoming connections on given socket (SERVER_IP, PORT) tuple:
s.bind((SERVER_IP, PORT))
s.listen()

print(f"Server is listening on {SERVER_IP}:{PORT}. Name: {SERVER_NAME}")

# CREATE A CLIENTS LIST
clients = set()

while True:
    (conn, addr) = s.accept()
    print(conn, addr)

    # ADD CLIENTS TO LIST
    clients.add(conn)

    # Each Client Connection should be handled in different thread
    tr = threading.Thread(target=receive_message, args=(conn,), daemon=True)
    # receive_message(conn)

    tr.start()


