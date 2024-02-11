class Cake:
    """This is clas representing a cake"""

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """To initialize a Cake object you need pass attributes like name, kind, taste and additives(which are list)
        and filling.

        init itself add a Cake object to a list of Cake objects
        """
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
        print('-'*20)

    @property
    def full_name(self):
        """To get the full name of the cake"""

        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


help(Cake)
help(Cake.full_name)
