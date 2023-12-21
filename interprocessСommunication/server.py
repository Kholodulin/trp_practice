import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Слушаем входящие соединения
server_socket.listen(1)
print(f"Server listening on {server_address}")

# Принимаем соединение
connection, client_address = server_socket.accept()
print(f"Connection from {client_address}")

data = connection.recv(1024)
print(f"Received: {data.decode()}")
connection.close()
