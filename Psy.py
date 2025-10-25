class dog():
    def __init__(self, name, rasa):
        self.name = name
        self.rasa = rasa
    def szczekaj(self):
        print(f"Hau Hau! Jestem {self.name} i jestem rasy {self.rasa}.")

pies_Spot = dog("Spot", "Beagle")
pies_Azor = dog("Azor", "Owczarek Niemiecki")   


pies_Spot.szczekaj()
pies_Azor.szczekaj()
