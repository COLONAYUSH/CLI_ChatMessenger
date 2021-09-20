import socket

PORT = 1234
IP = socket.gethostname()
# ip = socket.gethostname()
# print(ip)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
# message = s.recv(2048)
# print(message.decode("utf-8"))
msg = ''
while True:
    while True:
        message = s.recv(5)
        if len(message) == 0:
            break
        msg += message.decode("utf-8")
    print(msg)
