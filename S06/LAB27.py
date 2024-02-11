class Cake:
    def __init__(self, name: str, taste: str, additives: list, filling: str):
        self.name = name
        self.taste = taste
        self.additives = additives
        self.filling = filling


cake_01 = Cake('Tiramisu', 'coffe', ['coffe','chocolate sirup'], 'chocolate')
cake_02 = Cake('Apple Pie', 'fruit', ['apples'], 'apples')


bakery_offer = [cake_01, cake_02]

for cake in bakery_offer:
    print(cake.name, cake.taste, cake.additives, cake.filling)
