import socket
import keyboard

server_address = ('localhost', 12345)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print("Server is listening for a connection...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    try:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            client_socket.send(str(event).encode())
    except Exception as e:
        print(f"Error: {e}")
        break

server_socket.close()
