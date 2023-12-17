import tkinter as tk
from tkinter import messagebox


def ispisi(n, m, a):
    for i in range(n):
        for j in range(n + m):
            print('{:8.2f}'.format(a[i][j]), end='')
        print("")
    print("")


def show_solution(window, a):
    eps = 0.00001
    n = 3
    m = 1 + 3

    ispisi(n, m, a)

    # Gaus-Jordan eliminacija
    for k in range(n):
        # Da li je pivot element premali
        if abs(a[k][k]) <= eps:
            print("Mala vrednost pivot-a!")
            exit(0)

        # Normalizacija pivot reda
        for j in range(k + 1, n + m):
            a[k][j] = a[k][j] / a[k][k]
        a[k][k] = 1
        print("a[k][k]=a[%d][%d]=1, normalizacija reda %d" % (k, k, k))
        ispisi(n, m, a)

        # Eliminacija k-tog elementa osim pivota
        for i in range(n):
            if i == k or a[i][k] == 0:
                print("(i==k || a[i][k]==0), a[i][k]=a[%d][%d]=%6.2lf, continue" % (i, k, a[i][k]))
                ispisi(n, m, a)
                continue

            for j in range(k + 1, n + m):
                a[i][j] = a[i][j] - a[i][k] * a[k][j]
            print("a[i][j]=a[%d][%d]=%6.2lf racunanje a[i][j] - a[i][k] * a[k][j], k=%d" % (i, j, a[i][j], k))
            ispisi(n, m, a)

            a[i][k] = 0
            print("a[i][k]=a[%d][%d]=0, postavljanje nule" % (i, k))
            ispisi(n, m, a)
        print("Sledeca petlja, k=%d\n" % (k + 1))
        ispisi(n, m, a)


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
            r.geometry('300x300')
            show_solution(r, result)
        except ValueError:
            messagebox.showinfo("Info", "Vrednosti nisu dobre.")
