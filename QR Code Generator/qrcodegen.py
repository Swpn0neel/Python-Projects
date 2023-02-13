import tkinter as tk
import qrcode
from PIL import ImageTk, Image

class QRGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x400")

        # create entry widget for URL
        self.url_entry = tk.Entry(self.root)
        self.url_entry.pack(pady=10)

        # create a generate button
        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_qr)
        self.generate_button.pack(pady=10)

        # create an image label for QR code
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

    def generate_qr(self):
        url = self.url_entry.get()
        if not url:
            return

        # generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # display QR code in the image label
        imgtk = ImageTk.PhotoImage(img)
        self.image_label.config(image=imgtk)
        self.image_label.image = imgtk

if __name__ == '__main__':
    root = tk.Tk()
    qr_generator = QRGenerator(root)
    root.mainloop()