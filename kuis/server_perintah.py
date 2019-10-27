import socket, os
from threading import Thread

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind( ("127.0.0.1", 6666) )

tcp_sock.listen(100)

def handle_thread(conn) :
    while True:
        try :
            data = conn.recv(100)
            data = data.decode('ascii')
            print(data)

            conn.send( data.encode('ascii') )

            if data == "yes":
                conn.send( data.encode('ascii') )
             
            break

        except(socket.error):
            conn.close()
            print("koneksi diputus")
            break

while True :
    conn, client_addr = tcp_sock.accept()

    t=Thread(target=handle_thread, args=(conn,))
    t.start()
    
for t in Thread:
    t.join()