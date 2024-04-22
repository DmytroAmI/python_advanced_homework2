import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 12345))
data_in = input("Input text: ").encode("utf-8")
s.send(data_in)
s.close()
