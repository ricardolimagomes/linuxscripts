
#!/usr/bin/python

import socket, sys
try:
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1],sys.argv[2]))
	response = soc.recv(1024)
	print response

	soc.send("USER"+argv[3]+"\r\n")
	response2 = soc.recv(1024)
	print response2

	soc.send("PASS"+argv[4]+"\r\n")
	response3 = soc.recv(1024)
	print response3

	soc.send("QUIT\r\n")
	response4 = soc.recv(1024)
	print response4

except:
	print "Erro na conexao"
	print "Use: ip port USER PASSWORD"


