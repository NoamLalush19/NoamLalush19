import socket
import keyboard

server_address = ('localhost', 12345)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    try:
        data = client_socket.recv(1024).decode()
        keyboard.play(keyboard.read_event(s=data))
    except Exception as e:
        print(f"Error: {e}")
        break

client_socket.close()
