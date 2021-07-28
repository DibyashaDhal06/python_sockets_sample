import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
sock.bind(('localhost', 8080)) # gethostname is not too important here as we already know the hostname
sock.listen(10) # The number mentions how many connections to accept

print('Server is listening at ', sock.getsockname())
conn, address = sock.accept()
print("Connection established")
print("Connected to : ", address)
name = input('Name: ')
conn.send(name.encode())
rec = conn.recv(2048).decode('ascii')
print(rec,'has joined')
while True:
    try:
        msg = input('Server: ')
        sent = conn.send(msg.encode())# sends in byte form not in string
        message = conn.recv(2048).decode('ascii')
        print(rec,':',message)
        conn.close()
    except Exception as e:
        print(e)




