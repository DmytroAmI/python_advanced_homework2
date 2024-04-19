import socket

HOST = 'localhost'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        data_in = input('Enter two comma-separated numbers: ').encode("utf-8")
        if not data_in:
            break
        sock.sendall(data_in)
        out_data = sock.recv(1024)
        print('Sum:', out_data.decode('utf-8'))
