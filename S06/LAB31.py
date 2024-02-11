# is_on_sale = property(__GetIsOnSale, __SetIsOnSale. None, "if set to true, the car is available in sale/promo")


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name: str, kind: str, taste: str, additives: list, filling: str, gluten_free: bool, text: str):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
        if kind == 'cake':
            self.__text = text
        else:
            self.__text = ''
            print("Text can be only for cake")

        self.bakery_offer.append(self)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text: str):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print("Text can be only for cake")

    def show_info(self):
        print(f"Name: {self.name.capitalize()}")
        print(f"Kind: {self.kind}")
        print(f"Taste: {self.taste}")
        print(f'Is gluten_free: {self.__gluten_free}')
        print(f"Additives: {self.additives}") if len(self.additives) > 0 else print("No additives")
        print(f"Filling: {self.filling}") if self.filling else print("No filling")
        if len(self.__text) > 0:
            print(f"Text: {self.__text}")

        print('\n')

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives: list):
        self.additives += additives

    Text = property(__get_text, __set_text, None, 'Text on the cake')


cake_01 = Cake('Tiramisu', 'cake', 'coffe', ['coffe', 'chocolate sirup'], '', True, 'Happy')
cake_02 = Cake('Apple Pie','cake', 'fruit', ['apples'], 'apples', False,'Nice apple pie')
cake_04 = Cake('Cocoa waffle', 'muffin', 'waffle', ['cocoa'], 'cocoa', False,'Nice cocoa waffle')

for cake in Cake.bakery_offer:
    cake.show_info()


cake_01.Text = 'Birthday tiramisu'
cake_04.Text = 'cocoa'

for cake in Cake.bakery_offer:
    cake.show_info()
