import tkinter as tk
from resavanjeSistema import LinearEquationSolver


def solve_system():
    r = tk.Toplevel()
    labels = ["x", "y", "z","="]
    LinearEquationSolver(r, labels)


def show_image():
    # Logika za prikaz slike
    pass


root = tk.Tk()
root.geometry('300x300')

solve_system_button = tk.Button(root, text="Resavanje sistema jednacina", command=solve_system)
solve_system_button.pack(pady=10)


show_image_button = tk.Button(root, text="Prikaz slike", command=show_image)
show_image_button.pack(pady=10)

root.mainloop()
