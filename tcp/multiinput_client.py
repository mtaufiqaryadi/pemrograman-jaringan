import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect( ('127.0.0.1', 6666) )

for i in range(0,3):

    data = "selamat sore"
    tcp_sock.send( data.encode('ascii') )

    data = tcp_sock.recv(100)
    data = data.decode('ascii')

    print(data)

tcp_sock.close()