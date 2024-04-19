import socket

HOST = 'localhost'
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        try:
            data = sum([int(num) for num in data.decode('utf-8').split(',')])
            print(data)
            conn.sendall(str(data).encode('utf-8'))
        except ValueError:
            conn.sendall('Invalid input!'.encode('utf-8'))
