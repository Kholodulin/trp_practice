import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Отправляем данные серверу
message = "Hello, server!"
client_socket.sendall(message.encode())
print(f"Sent: {message}")

client_socket.close()
