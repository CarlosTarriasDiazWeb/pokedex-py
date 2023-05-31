import tkinter as tk
import json


class PokemonCards(tk.Frame):
    def __init__(self, parent, pokemon):
        super().__init__()

        column = 0
        row = 0

        for poke in pokemon:
            pokemon_card = tk.Frame(parent, width=120, height=120, background="white")
            pokemon_card.grid(row=row, column=column, padx=5, pady=5, columnspan=2)

            pokemon_id = tk.Label(pokemon_card, text=poke["id"], background="white")
            pokemon_id.grid(row=0, column=0, padx=3, pady=3)

            pokemon_name = tk.Label(pokemon_card, text=poke["name"], background="white")
            pokemon_name.grid(row=1, column=0, padx=3, pady=3)

            pokemon_description = tk.Label(pokemon_card, text=poke["description"], wraplength=250, background="white", )
            pokemon_description.grid(row=2, column=0, padx=3, pady=3)

            column += 1
            if column == 3:
                column = 0
                row += 1
