import socket

s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind((host,port))

s.listen(5)
while True:
	connect, address = s.accept()
	print('got connection from', address)
	data = 'hello client'
	connect.send(data.encode())
	print(connect.recv(1024).decode())
	connect.close()