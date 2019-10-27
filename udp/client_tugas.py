import socket

upd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# inisiasi variabel data dan address
data = input("today/yesterday/tomorrow : ")
server_addr = ("127.0.0.1", 6666)
# kirim data ke server
upd_sock.sendto(data.encode('ascii'), server_addr)
# baca data yang dikembalikan server
data = upd_sock.recv(100)
data = data.decode('ascii')
print(data)