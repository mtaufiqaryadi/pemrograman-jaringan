import socket

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_sock.bind( ("0.0.0.0", 6666) )

while True:
    tanggal = 22
    data, client_addr = udp_sock.recvfrom(1000)
    #Konversi dari bytes jadi string
    data = data.decode('ascii')
    
    if data == 'today':
        tanggal = 22
    elif data == 'yesterday' :
        tanggal -= 1
    elif data == 'tomorrow' :
        tanggal += 1
    print(data)
    #Olah string
    data = str(tanggal)
    #Kirim balik ke client
    udp_sock.sendto ( data.encode('ascii'), client_addr)