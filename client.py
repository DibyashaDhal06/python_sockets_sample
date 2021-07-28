import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080)) # Notice how we don't need to bother with FQDN here
print("Connected")
name = input('Enter your name: ')
sent = sock.send(name.encode()) # We use endline as a common terminator
resp = sock.recv(2048).decode('ascii')
print(resp, "has connected ")
while True:
    msg = input('Client:' )
    sent = sock.send(msg.encode())# sends in byte form not in string
    message = sock.recv(2048).decode('ascii')
    print(resp,':',message)
    
    

sock.close()


