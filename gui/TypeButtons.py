import tkinter as tk

types = (
    ("FIRE", "red"),
    ("GHOST", "white"),
    ("WATER", "cyan"),
    ("FIGHTING", "brown"),
    ("FAIRY", "pink"),
    ("POISSON", "magenta"),
    ("ELECTRIC", "yellow"),
    ("ICE", "lightblue"),
    ("GRASS", "lightgreen")
)


class TypeButtons(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        filter_buttons = []

        for i in range(len(types)):
            b = tk.Button(parent, text=types[i][0], background=types[i][1], width=10)
            b.grid(row=i + 2, column=0, sticky=tk.W, padx=5, pady=5, columnspan=2)
            filter_buttons.append(b)
