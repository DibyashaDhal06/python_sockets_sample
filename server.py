import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080)) # gethostname is not too important here as we already know the hostname
sock.listen(10) # The number mentions how many connections to accept

print('Server is listening at ', sock.getsockname())
while True:
    resp = ''
    conn, address = sock.accept()
    print("Connected to : ", address)
    try:
        resp = conn.recv(2048).decode('ascii')
        print("Recieved : ", resp)
        sent = conn.send(b'world')
        print(sent)
        conn.close()
    except Exception as e:
        print(e)
