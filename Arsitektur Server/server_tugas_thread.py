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
            data = data.split()
            perintah = data[0]
            nama_file = data[1]
            print(perintah)
            print(nama_file)

            if perintah == "new":
                f= open(nama_file+".txt","w+")
                for i in range(2):
                    f.write("This is line %d\r\n" % (i+1))
                data = "OK"
                f.close()

            elif perintah == "del":
                os.remove(nama_file+".txt")
                data = "OK"
                
            elif perintah == "read": 
                f= open(nama_file+".txt","r")
                data = f.read()
                f.close()

            conn.send( data.encode('ascii') )

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