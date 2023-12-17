import tkinter as tk
from tkinter import messagebox


def ispisi(n, m, a):
    s = ""
    for i in range(n):
        for j in range(n + m):
            s += '{:8.2f} '.format(a[i][j])
        s += '\n'
    s += '\n'
    return s


def show_solution(r, a):
    v = tk.Scrollbar(r)
    v.pack(side='right', fill='y')

    t = tk.Text(r, width=15, height=20, wrap=tk.NONE, yscrollcommand=v.set)

    m = 1 + 3
    n = 3
    t.insert(tk.END, f"1. Pocetna matrica je: \n{ispisi(n, m, a)}")
    t.pack(side=tk.TOP, fill=tk.X)
    eps = 0.00001

    # Gaus-Jordan
    for k in range(n):
        # Da li je pivot element premali
        t.insert(tk.END, f"2. Da li je pivot element premali?\n")
        t.pack(side=tk.TOP, fill=tk.X)
        if abs(a[k][k]) <= eps:
            messagebox.showerror("Error", "Mala vrednost pivot-a!")
            exit(0)
        t.insert(tk.END, f" Nije.\n")
        t.pack(side=tk.TOP, fill=tk.X)
        # Normalizacija pivot reda
        t.insert(tk.END, f"3. Normalizacija pivot reda: \n")
        t.pack(side=tk.TOP, fill=tk.X)
        for j in range(k + 1, n + m):
            a[k][j] = a[k][j] / a[k][k]
        a[k][k] = 1
        t.insert(tk.END, "a[k][k]=a[{}][{}]=1, normalizacija reda {}\n".format(k, k, k) + f"{ispisi(n, m, a)}")
        t.pack(side=tk.TOP, fill=tk.X)

        # Eliminacija k-tog elementa osim pivota
        t.insert(tk.END, f"4. Eliminacija k-tog elementa osim pivota: \n")
        t.pack(side=tk.TOP, fill=tk.X)
        for i in range(n):
            if i == k or a[i][k] == 0:
                t.insert(tk.END, "(i==k || a[i][k]==0), a[i][k]=a[{}][{}]={:.2f}, nastavi..\n".format(i, k, a[i][
                    k]) + f"{ispisi(n, m, a)}")
                t.pack(side=tk.TOP, fill=tk.X)
                continue

            for j in range(k + 1, n + m):
                a[i][j] = a[i][j] - a[i][k] * a[k][j]
                t.insert(tk.END, "a[i][j]=a[{}][{}]={:.2f} racunanje a[i][j] - a[i][k] * a[k][j],"
                                 " k={}\n".format(i, j, a[i][j], k) + f"{ispisi(n, m, a)}")
                t.pack(side=tk.TOP, fill=tk.X)

            a[i][k] = 0
            t.insert(tk.END, "a[i][k]=a[{}][{}]=0, postavljanje nule\n".format(i, k) + f"{ispisi(n, m, a)}")
            t.pack(side=tk.TOP, fill=tk.X)

        t.insert(tk.END, "Sledeca petlja, k={}\n".format(k + 1))
        t.pack(side=tk.TOP, fill=tk.X)
    t.insert(tk.END, f"Konacna matrica je: \n{ispisi(n, m, a)}")
    t.pack(side=tk.TOP, fill=tk.X)


class LinearEquationSolver:
    def __init__(self, master, labels, num_equations=3):
        self.master = master
        self.labels = labels
        self.num_equations = num_equations

        self.entry_rows = []
        self.variables = []
        self.operators_var = []

        self.create_widgets()

    def create_entry_row(self):
        row_frame = tk.Frame(self.master)
        operators = ["+", "-"]

        variables_row = [tk.StringVar(value="") for _ in range(len(self.labels))]
        operators_row = [tk.StringVar(value=operators[0]) for _ in range(len(self.labels))]

        for i, label in enumerate(self.labels[:-1]):
            tk.OptionMenu(row_frame, operators_row[i], *operators).pack(side=tk.LEFT)
            tk.Entry(row_frame, textvariable=variables_row[i], width=5).pack(side=tk.LEFT)
            tk.Label(row_frame, text=label).pack(side=tk.LEFT)

        tk.Label(row_frame, text=self.labels[-1]).pack(side=tk.LEFT)
        tk.OptionMenu(row_frame, operators_row[-1], *operators).pack(side=tk.LEFT)
        tk.Entry(row_frame, textvariable=variables_row[-1], width=5).pack(side=tk.LEFT)

        row_frame.pack(pady=5)
        self.entry_rows.append(row_frame)
        self.variables.append(variables_row)
        self.operators_var.append(operators_row)

    def create_widgets(self):
        self.master.title("Unos sistema linearnih jednačina")
        for _ in range(self.num_equations):
            self.create_entry_row()
        show_values_button = tk.Button(self.master, text="Prikaži unete vrednosti",
                                       command=self.show_entered_values)
        show_values_button.pack(pady=10)
        solve_button = tk.Button(self.master, text="Reši sistem", command=self.solve_system)
        solve_button.pack(pady=10)

    def show_entered_values(self):
        for i, (row_frame, vars_row, ops_row) in enumerate(zip(self.entry_rows, self.variables, self.operators_var)):
            variables_row = [var.get() for var in vars_row]
            operators_row = [op.get() for op in ops_row]
            print(f"Entry[{i}] = {variables_row}, Operator[{i}] = {operators_row}")

    def solve_system(self):
        try:
            matrix = []
            ones_matrix = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
            for i, (row_frame, vars_row, ops_row) in enumerate(
                    zip(self.entry_rows, self.variables, self.operators_var)):
                variables_row = [float(var.get()) for var in vars_row]
                operators_row = [op.get() for op in ops_row]
                matrix.append([entry if op == '+' else -entry for entry, op in zip(variables_row, operators_row)])
            result = [matrix[i] + ones_matrix[i] for i in range(3)]
            r = tk.Toplevel(self.master)
            r.geometry('900x400')
            show_solution(r, result)
        except ValueError:
            messagebox.showinfo("Info", "Vrednosti nisu dobre.")
