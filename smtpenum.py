
#!/usr/bin/python
import socket, sys

file = open('listasmtp.txt')
for linha in file.readlines();
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1],25))
	s.send("VRFY "+linha)
	resp = s.recv(1024)
	print resp
