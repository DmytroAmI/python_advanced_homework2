import socket

HOST = 'localhost'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

while True:
    try:
        client, addr = s.accept()
    except KeyboardInterrupt:
        print('Closing')
        socket.close(s)
        break
    else:
        data = client.recv(1024)
        print(addr, ">>",  data.decode('utf-8'))
        client.close()
