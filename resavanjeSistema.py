import tkinter as tk


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
            tk.Label(row_frame, text=label).pack(side=tk.LEFT)
            tk.Entry(row_frame, textvariable=variables_row[i], width=5).pack(side=tk.LEFT)

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
        solve_button = tk.Button(self.master, text="Reši sistem", command=solve_system)
        solve_button.pack(pady=10)

    def show_entered_values(self):
        for i, (row_frame, vars_row, ops_row) in enumerate(zip(self.entry_rows, self.variables, self.operators_var)):
            variables_row = [var.get() for var in vars_row]
            operators_row = [op.get() for op in ops_row]
            print(f"Entry[{i}] = {variables_row}, Operator[{i}] = {operators_row}")


def solve_system():
    # Ovde možete dodati logiku za rešavanje sistema linearnih jednačina
    pass
