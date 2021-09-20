import socket

PORT = 1234
IP = socket.gethostname()
# ip = socket.gethostname()
# print(ip)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((IP, PORT))
s.listen(5)
while True:
    client_socket, address = s.accept()
    client_socket.send(bytes("Its working fine!", "utf-8"))
    print(f'Connection with client {address} has been established')
    client_socket.close()
