import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
# import numpy as np


class SharpenFrame(tk.Frame):
    def __init__(self, master, filename="tiger.jpg"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.filename = filename
        self.imgObj = None
        self.lblImage = None
        self.lblShrpn = None
        self.txt = tk.Label(self, text="Hello")
        self.txt.pack()
        self.sharpen_multiplier = tk.IntVar()
        self.sharpen_multiplier.set(1)
        # self.sharpen_kernel = np.array(list(ImageFilter.SHARPEN().filterargs[3])) # custom kernel
        self.spinbox = tk.Spinbox(self, command=self.spinbox_changed, from_=1, to=10, width=3,
                                  textvariable=self.sharpen_multiplier)
        self.spinbox.pack()
        self.image_open()
        self.image_sharpen()
        self.pack(expand=True, fill=tk.BOTH)

    def spinbox_changed(self):
        self.lblShrpn.pack_forget()
        self.image_sharpen()
        pass

    def image_open(self):
        self.imgObj = Image.open(self.filename).filter(ImageFilter.BLUR)
        image = ImageTk.PhotoImage(self.imgObj)
        self.lblImage = tk.Label(self, image=image)
        self.lblImage.image = image
        self.lblImage.pack()
        self.pack()

    def image_sharpen(self):
        # shrpn = self.imgObj.filter(ImageFilter.Kernel((3, 3), self.sharpen_kernel)) # custom kernel
        shrpn = self.imgObj.filter(ImageFilter.SHARPEN)
        for i in range(self.sharpen_multiplier.get()-1):
            # shrpn = shrpn.filter(ImageFilter.Kernel((3, 3), self.sharpen_kernel)) # custom kernel
            shrpn = shrpn.filter(ImageFilter.SHARPEN)
        image_sharpened = ImageTk.PhotoImage(shrpn)
        self.lblShrpn = tk.Label(self, image=image_sharpened)
        self.lblShrpn.image = image_sharpened
        self.lblShrpn.pack()
        self.pack()
