import socket
import pyautogui

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        parts = data.split()
        action = parts[0]

        if action == 'move':
            x, y = map(int, parts[1:])
            pyautogui.moveTo(x, y)

        elif action == 'click':
            x, y, button = map(int, parts[1:])
            pyautogui.click(x, y, button=button)

except KeyboardInterrupt:
    pass

client_socket.close()
