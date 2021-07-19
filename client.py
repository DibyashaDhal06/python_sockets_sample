import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080)) # Notice how we don't need to bother with FQDN here

sent = sock.send("hello".encode()) # We use endline as a common terminator
print(sent)
resp = sock.recv(2048)
print("Recieved ", resp)

# sock.close()
