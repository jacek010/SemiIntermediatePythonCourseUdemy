class Cake:
    def __init__(self, name: str, taste: str, additives: list, filling: str):
        self.name = name
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print(f"Name: {self.name.capitalize()}")
        print(f"Taste: {self.taste}")
        print(f"Additives: {self.additives}") if len(self.additives) > 0 else print("No additives")
        print(f"Filling: {self.filling}\n\n") if self.filling else print("No filling\n\n")

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives: list):
        self.additives += additives


cake_01 = Cake('Tiramisu', 'coffe', ['coffe', 'chocolate sirup'], '')
cake_02 = Cake('Apple Pie', 'fruit', ['apples'], 'apples')

bakery_offer = [cake_01, cake_02]

for cake in bakery_offer:
    cake.show_info()
    cake.set_filling('tasty filling')
    cake.add_additives(['flavour', 'water'])
    cake.show_info()
