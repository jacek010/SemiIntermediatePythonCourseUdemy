class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print("Occasion: {}".format(self.occasion))
        print("Shape: {}".format(self.shape))
        print("Ornaments: {}".format(self.ornaments))
        print("Text: {}".format(self.text))


birthday = SpecialCake('birthday', 'cake', 'coffe', ['milk, chocolate'], 'coffe',
                       'birthday', 'square', 'flowers', 'Happy Birthday!')
wedding = SpecialCake('wedding', 'cake', 'strawberry', ['milk, strawberries'], 'jam',
                      'wedding party', 'rounded', 'hearts', 'Mr.XXX and Ms.YYY!')

birthday.show_info()
wedding.show_info()

for c in SpecialCake.bakery_offer:
    print(c.full_name)
    c.show_info()
    print('\n\n')
