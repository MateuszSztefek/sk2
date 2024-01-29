import socket

HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.11"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive_file():
    file_name = client.recv(1024).decode()
    if "file doesn't exist" in file_name:
        print("file doesn't exist")
        return

    file = open(file_name, "wb")
    file_bytes = b""
    done = False

    while not done:
        if file_bytes[-5:] == b"<END>":
            done = True
        else:
            data = client.recv(1024)
            file_bytes += data

    file.write(file_bytes)

    print("Downloading done")
    file.close()


def handle_list_of_files():
    print(client.recv(2048).decode())


def send(msg):
    message = msg.encode()
    msg_length = len(message)
    send_length = str(msg_length).encode()
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if msg[:5] == "!SHOW":
        handle_list_of_files()
    if msg[:4] == "!GET":
        receive_file()


print("Viable commands: !SHOW, !GET filename, !DISCONNECT")
while True:
    print("->", end="")
    command = input()
    send(command)
    if command == "!DISCONNECT":
        break
