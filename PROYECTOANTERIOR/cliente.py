import socket

HOST = "127.0.0.1" #192.168.100.43
PORT = 65432

# Crear socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

mensaje = input("Escribe la categoría que deseas (deportes, noticias, clima): ").lower()
client_socket.sendall(mensaje.encode())

respuesta = client_socket.recv(1024).decode()
print(f"Respuesta del servidor: {respuesta}")

client_socket.close()
