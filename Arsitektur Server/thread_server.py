import socket
from threading import Thread

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind( ("0.0.0.0", 6666) )

tcp_sock.listen(100)

def handle_thread(conn) :
    while True:
        try :
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data

            conn.send( data.encode('ascii') )
        except(socket.error):
            conn.close()
            print("koneksi diputus")
            break

while True :
    conn, client_addr = tcp_sock.accept()

    t=Thread(target=handle_thread, args=(conn,))
    t.start()