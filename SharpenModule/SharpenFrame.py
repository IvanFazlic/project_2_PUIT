import tkinter as tk
from PIL import Image, ImageTk, ImageFilter


class SharpenFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="red")
        self.master=master
        self.txt = tk.Label(self, text="Hello")
        self.txt.pack()
        self.pack(expand=True, fill=tk.BOTH)