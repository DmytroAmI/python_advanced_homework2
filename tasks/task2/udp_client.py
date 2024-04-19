import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(b'127.0.0.1', ('127.0.0.1', 9999))
