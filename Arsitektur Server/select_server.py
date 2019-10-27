import socket
import select

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind( ("0.0.0.0", 6666) )

tcp_sock.listen(100)

list_monitor = [ tcp_sock ]

while True : 

    inputready, outputready, errorready = select.select(list_monitor, [], [])

    for conn in inputready:

        if conn == tcp_sock :
            conn, client_addr = tcp_sock.accept()
            list_monitor.append(conn)
        
        else: 
            try:
                data = conn.recv(100)
                data = data.decode('ascii')
                data = "OK "+data

                conn.send( data.encode('ascii') )
            except(socket.error):
                conn.close()

                list_monitor.remove(conn)
                print("koneksi telah dihapus")