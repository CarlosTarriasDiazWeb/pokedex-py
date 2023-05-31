import json
import tkinter as tk
from PokemonCards import PokemonCards
from TypeButtons import TypeButtons


# Create Classes for GUI component

# TODO....

class MainApplication(tk.Frame):
    def __init__(self):
        super().__init__()
        self.cards = self.get_pokemon()

        types_frame = tk.Frame(root, width=200, height=610, background="#616161")
        types_frame.grid(row=0, column=0, padx=10, pady=15)
        tk.Label(types_frame, text="Filter by Type", background="#616161").grid(row=1, column=0, padx=5, pady=5)
        TypeButtons(types_frame)

        pokemon_frame = tk.Frame(root, width=1000, height=610, background="gray")
        pokemon_frame.grid(row=0, column=1, padx=10, pady=15)
        PokemonCards(pokemon_frame, self.cards)

    @staticmethod
    def get_pokemon():
        with open("pokemon_data.json") as pokemon_data:
            data_reader = json.load(pokemon_data)
        return data_reader


def set_dims(root):
    root.title("Pokedex Filter")
    root.config(bg="#313131")
    root.geometry("860x640")
    root.resizable(0, 0)


if __name__ == "__main__":
    root = tk.Tk()
    set_dims(root)
    app = MainApplication()
    root.mainloop()

# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
# https://stackoverflow.com/questions/17466561/what-is-the-best-way-to-structure-a-tkinter-application
# https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
