import socket, os

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind( ("0.0.0.0", 6666) )

tcp_sock.listen(100)

while True :
    conn, client_addr = tcp_sock.accept()

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

conn.close()