import socket               

HOST = ''                 
PORT = 8666              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print 'Listening to port 8666'
s.listen(1)
while True: 
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()