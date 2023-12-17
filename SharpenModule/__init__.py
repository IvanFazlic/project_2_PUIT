if __name__ == "__main__":
    from SharpenFrame import SharpenFrame as SFrame
    import tkinter as tk

    app = tk.Tk()
    sf = SFrame(app)
    app.mainloop()
else:
    from .SharpenFrame import SharpenFrame
