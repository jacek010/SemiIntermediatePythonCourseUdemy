class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []
    def __init__(self, name: str, taste: str, additives: list, filling: str):
        if name in self.known_types:
            self.name = name
        else:
            self.name = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)


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
cake_04 = Cake('Cocoa waffle', 'waffle', ['cocoa'], 'cocoa')


for cake in Cake.bakery_offer:
    cake.show_info()


print('Is cake01 of type Cake? (isinstance)', isinstance(cake_01, Cake))
print('Is cake01 of type Cake? (type)', type(cake_01) is Cake)
print('vars cake01', vars(cake_01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake_01))
print('dir Cake?', dir(Cake))
