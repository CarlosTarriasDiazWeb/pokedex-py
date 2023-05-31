# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
from TypeButtons import TypeButtons


# Create Classes for GUI component

# TODO....

class MainApplication(tk.Frame):
    def __init__(self):
        super().__init__()
        self.pack(fill=tk.BOTH, expand=True)
        # FILTER BUTTONS
        TypeButtons(self)

        # set components as attributes


def set_dims(parent):
    parent.geometry("860x640")
    parent.title("Pokedex Filter")
    parent.resizable(0, 0)


if __name__ == "__main__":
    root = tk.Tk()
    set_dims(root)
    app = MainApplication()
    root.mainloop()

# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
# https://stackoverflow.com/questions/17466561/what-is-the-best-way-to-structure-a-tkinter-application
