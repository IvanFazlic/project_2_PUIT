import copy
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageDraw, ImageFont
# import numpy as np


class SharpenFrame(tk.Frame):
    def __init__(self, master: tk.Toplevel, filename="tiger.jpg"):
        tk.Frame.__init__(self, master)
        # master setup
        self.master = master
        self.master.title("Primena sharpen filtera nad slikom")
        self.master.minsize(283,200)
        # class setup
        self.filename = filename
        self.imgObjOrig = None
        self.imgObj = None
        self.lblImage = None
        self.lblShrpn = None
        # control setup
        self.control = tk.Frame(self)
        self.control.columnconfigure(2, weight=1)
        self.lblSharpenText = tk.Label(self.control, text="Multiplier za sharpen filter:")
        self.lblSharpenText.grid(row=0, column=0)
        self.sharpen_multiplier = tk.IntVar()
        self.sharpen_multiplier.set(1)
        # self.sharpen_kernel = np.array(list(ImageFilter.SHARPEN().filterargs[3])) # custom kernel
        self.spinbox = tk.Spinbox(self.control, command=self.spinbox_changed, from_=0, to=10, width=3,
                                  textvariable=self.sharpen_multiplier)
        self.spinbox.grid(row=0, column=1)
        self.btnBrowse = tk.Button(self.control, text="Otvori novu sliku", command=self.browse_clicked)
        self.btnBrowse.grid(row=0, column=3, sticky="NS")
        self.control.grid(row=0, column=0,sticky="new")
        # images setup
        self.font = ImageFont.truetype("arial.ttf", size=20)
        self.width = 400
        self.height = 226
        self.images = tk.Frame(self)
        self.image_open()
        self.image_sharpen()
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0, weight=1)
        self.images.bind("<Configure>", self.resize)
        self.images.grid(row=1, column=0, sticky="nsew")
        self.pack(expand=True, fill=tk.BOTH)


    def resize(self, event):
        #print(event.width, event.height)
        self.width=event.width-4
        self.height = int((event.height-8)/2)
        self.reloadBoth()
    def reloadBoth(self):
        self.lblImage.grid_forget()
        self.lblShrpn.grid_forget()
        self.image_open()
        self.image_sharpen()
    def browse_clicked(self):
        self.filename = tk.filedialog.askopenfilename()
        self.reloadBoth()
        pass

    def spinbox_changed(self):
        self.lblShrpn.grid_forget()
        self.image_sharpen()
        pass

    def fit(self):
        image_AR = self.imgObjOrig.width/self.imgObjOrig.height
        window_AR = self.width/self.height
        if image_AR < window_AR:
            return True
        else:
            return False

    def image_open(self):
        self.imgObjOrig = Image.open(self.filename)
        if self.fit():
            self.imgObj = self.imgObjOrig.resize((int(self.imgObjOrig.width / self.imgObjOrig.height * self.height)+1,
                                                  self.height))
        else:
            self.imgObj = self.imgObjOrig.resize((self.width,
                                                  int(self.imgObjOrig.height/self.imgObjOrig.width*self.width)))
        img = copy.deepcopy(self.imgObj)
        ImageDraw.Draw(img).text((10, 10), "Original", fill=(255, 0, 0), font=self.font)
        image = ImageTk.PhotoImage(img)
        self.lblImage = tk.Label(self.images, image=image)
        self.lblImage.image = image
        #self.lblImage.pack()
        self.lblImage.grid(row=1, column=0,sticky="nsew")
        self.pack()

    def image_sharpen(self):
        # shrpn = self.imgObj.filter(ImageFilter.Kernel((3, 3), self.sharpen_kernel)) # custom kernel
        shrpn = self.imgObj
        for i in range(self.sharpen_multiplier.get()):
            # shrpn = shrpn.filter(ImageFilter.Kernel((3, 3), self.sharpen_kernel)) # custom kernel
            shrpn = shrpn.filter(ImageFilter.SHARPEN)
        sharpened = copy.deepcopy(shrpn)
        ImageDraw.Draw(sharpened).text((10, 10), "Sharpened", fill=(255, 0, 0), font=self.font)
        image_sharpened = ImageTk.PhotoImage(sharpened)
        self.lblShrpn = tk.Label(self.images, image=image_sharpened)
        self.lblShrpn.image = image_sharpened
        self.lblShrpn.grid(row=2,column=0,sticky="nsew")
        self.pack()
