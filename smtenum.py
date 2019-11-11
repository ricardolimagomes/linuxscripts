
#!/usr/bin/python
import socket,sys

if len(sys.argv) != 3:
	print "Use: python smtenum.py IP USER"
	sys.exit(0)


ip = sys.argv[1]
user = sys.argv[2]



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,25))
banner = s.recv(1024)
print banner

s.send("VRFY "+user+"\r\n")
r = s.recv(1024)
print r
