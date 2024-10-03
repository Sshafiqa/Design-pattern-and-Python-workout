# Example 1.1
# Server
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to an IP address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(1)
print("Server listening on port 12345...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Receive data from the client
data = conn.recv(1024)
print(f"Received from client: {data.decode()}")

# Send a response to the client
conn.sendall(b"Hello, Client!")

# Close the connection
conn.close()import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send data to the server
client_socket.sendall(b"Hello, Server!")

# Receive response from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Close the connection
client_socket.close()


# Client
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send data to the server
client_socket.sendall(b"Hello, Server!")

# Receive response from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Close the connection


# Example 1.2
# Server
Copy code
import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the server to an IP address and port
server_socket.bind(('localhost', 12345))
print("UDP Server listening on port 12345...")

# Receive data from the client
data, addr = server_socket.recvfrom(1024)
print(f"Received from client: {data.decode()}")

# Send a response to the client
server_socket.sendto(b"Hello, UDP Client!", addr)

# Client
import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
client_socket.sendto(b"Hello, UDP Server!", ('localhost', 12345))

# Receive response from the server
data, addr = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")


