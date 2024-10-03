# Example 2.1
import socket
import threading

def handle_client(conn, addr):
    print(f"Handling connection from {addr}")
    data = conn.recv(1024)
    print(f"Received: {data.decode()}")
    conn.sendall(b"Response from server")
    conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server is listening...")

while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()

# Example 2.2
import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setblocking(0)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

inputs = [server_socket]
outputs = []

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server_socket:
            conn, addr = s.accept()
            print(f"New connection from {addr}")
            conn.setblocking(0)
            inputs.append(conn)
        else:
            data = s.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
                if s not in outputs:
                    outputs.append(s)
            else:
                inputs.remove(s)
                s.close()

    for s in writable:
        s.send(b"Response from server")
        outputs.remove(s)
