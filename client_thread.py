import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))
print("Connected")

while True:
    name = input('Enter your name: ')
    sent = sock.send(name.encode())
    resp = sock.recv(2048).decode('ascii')
    print(resp, "has connected ")

sock.close()
