import socket
import _thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
sock.bind(('localhost', 8080))
count = 0
resp = ''
sock.listen(10)


def thread_func(conn):
    while True:
        resp = conn.recv(2048).decode('ascii')
        print(resp,"has joined")
        sent = conn.sendall(name.encode())
        print(sent)
    conn.close()

while True:
    conn, address = sock.accept()
    print("Connection established")
    print("Connected to : ", address)
    _thread.start_new_thread(thread_func, (conn, ))
    count += 1
    print('Thread count: ',count)
sock.close()
