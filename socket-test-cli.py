import socket

s = socket.socket()

host = socket.gethostbyname(input('Enter server address: '))

port = 12345

s.connect((host, port))

msg = s.recv(1024)

print(msg.decode('ascii'))

s.close()