import socket
import tkinter
from PIL import Image, ImageTk
from io import BytesIO

class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.label = tkinter.Label(self.root)
        self.label.pack()
        self.init_connection()
        self.update_image()
        self.root.mainloop()

    def init_connection(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('0.0.0.0', 10000)
        sock.bind(server_address)
        sock.listen(1)
        self.connection, _ = sock.accept()

    def update_image(self):
        size_bytes = self.connection.recv(4)
        size = int.from_bytes(size_bytes, byteorder='big')

        image_bytes = self.connection.recv(size)

        try:
            image = Image.open(BytesIO(image_bytes))
            photo_image = ImageTk.PhotoImage(image)
            self.label.config(image=photo_image)
            self.label.image = photo_image
        except:
            pass

        self.root.after(10, self.update_image)

App()
