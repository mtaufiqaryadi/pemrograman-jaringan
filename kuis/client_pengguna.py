import socket
import sys

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect( ('127.0.0.1', 6666) )

perintah = input("on/off : ")
nama_file = sys.argv[1]
data = perintah + " " + nama_file

tcp_sock.send( data.encode('ascii') )

data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)

tcp_sock.close()