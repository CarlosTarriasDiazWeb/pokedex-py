import tkinter as tk

types = (("FIRE", "red"), ("WATER", "cyan"), ("ICE", "lightblue"), ("GRASS", "lightgreen"))


class TypeButtons(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        filter_row = tk.Frame(parent)
        filter_row.pack(fill=tk.X)

        filter_buttons = []
        for type in types:
            b = tk.Button(filter_row, text=type[0], background=type[1])
            b.pack(side=tk.LEFT, padx=5, pady=5)
            filter_buttons.append(b)
