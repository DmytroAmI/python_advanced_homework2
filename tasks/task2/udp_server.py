import socket

HOST = '127.0.0.1'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print('connection by', data.decode('utf-8'))
