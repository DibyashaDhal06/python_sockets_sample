import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080)) # Notice how we don't need to bother with FQDN here
print("Connected")
name = input('Enter your name: ')
sent = sock.send(name.encode()) # We use endline as a common terminator
print("Sent to server:", sent)
resp = sock.recv(2048).decode('ascii')
print(resp, "has connected ")
sock.close()
