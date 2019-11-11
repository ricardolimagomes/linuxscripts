
#!/usr/bin/python
import socket
import sys
param = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((param,21))
response = s.recv(1024)
print response

s.send("USER anonymous\r\n")
response2 = s.recv(1024)
print response2

s.send("PASS anonymous\r\n")
response3 = s.recv(1024)
print response3

s.send("PWD \r\n")
s.send("QUIT \r\n")
response4 = s.recv(2048)
print response4

