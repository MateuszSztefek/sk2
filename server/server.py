import socket
import threading
import os

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def show_files(conn, addr):
    print(f"[LISTING ALL FILES] for {addr}")
    files = os.listdir()
    files.remove("server.py")
    conn.send(f"All files: {files}".encode())


def send_file(conn, addr, msg):
    file_name = msg.split(" ")
    file_name = file_name[1]
    print(f"[SENDING FILE] {file_name} to {addr}")
    if not os.path.isfile(file_name):
        print(f"File {file_name} doesn't exist")
        conn.send("file doesn't exist".encode())
        return

    file = open(file_name, "rb")

    conn.send(file_name.encode())

    data = file.read()
    conn.sendall(data)

    conn.send(b"<END>")
    file.close()


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode()

            print(f"[{addr}] {msg}")

            if msg == "!DISCONNECT":
                connected = False
            if msg == "!SHOW":
                show_files(conn, addr)
            if msg[:4] == "!GET":
                send_file(conn, addr, msg)

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
