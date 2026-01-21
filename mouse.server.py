import socket
import pyautogui
from pynput.mouse import Listener, Controller

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

client_socket, client_address = server_socket.accept()
print(f"Client {client_address} connected")

mouse = Controller()
last_x, last_y = pyautogui.position()

def on_move(x, y):
    global last_x, last_y
    if x != last_x or y != last_y:
        last_x, last_y = x, y
        message = f"move {x} {y}"
        client_socket.send(message.encode('utf-8'))

def on_click(x, y, button, pressed):
    if pressed:
        message = f"click {x} {y} {button}"
        client_socket.send(message.encode('utf-8'))
        mouse.position = (x, y)
        mouse.click(button)

with Listener(on_move=on_move, on_click=on_click) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass

server_socket.close()
