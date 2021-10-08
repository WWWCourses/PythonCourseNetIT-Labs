import socket
import threading

PORT = 5050
# IN ORDER TO START YOUR SERVER AND CONNECT TO IT, SERVER_NAME HAS TO BE HARDCORDED BY YOUR OWN SERVER NAME
# IN MY CASE IT'S dimitar-hristov86 or YOU CAN GET IT--> SERVER_NAME = socket.gethostname()
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
CLIENT_NAME = socket.gethostname()
CLIENT_IP = socket.gethostbyname(CLIENT_NAME)
ENCODING = "utf-8"

BUF_SIZE = 1024


def send_message(msg):
    s.send(msg.encode(ENCODING))


# define an INET (i.e. IPv4), STREAMing (i.e. TCP) socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# now connect to the server given with (SERVER_IP, PORT) tupple:
s.connect((SERVER_IP, PORT))
print(f'Client is connected to {(SERVER_IP, PORT)} ')
print(f'Client IP: {CLIENT_IP}, NAME: {CLIENT_NAME} ')

user_name = input('Enter your name: ')

# TASK: Receive messages from server and print them

def receive_message():
    while True:
        try:
            msg_bytes = s.recv(BUF_SIZE)
            msg = msg_bytes.decode(ENCODING)
            if msg == "":
                print("Server is down!")
                exit(0)
            print(f'Received: ', msg)
        except Exception as e:
            print(f'Error: {e}')
            break
            s.close()

# receive_message()
tr = threading.Thread(target=receive_message, daemon=True)
tr.start()


while True:
    msg = input("Enter message:")
    # EMPTY MESSAGES SHOULDN'T BE SENT TO SERVER
    if msg == "":
        print('Empty messages do not send to server! Try again')
        pass
    else:
        send_message(f'{user_name}>>>{msg}')
