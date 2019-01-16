class Computer:

    def __init__(self, regular_price, __default_price):
        self.regular_price = regular_price
        self.__default_price = __default_price

    def print_all_prices(self):
        return 'regular_price: {},  Default price: {}'.format(self.regular_price, self.__default_price)

    def set_default_price(self, my_price):
        self.__default_price = my_price

    def get_default_price(self):
        return self.__default_price


pass

c = Computer(15, 30)
print(c.print_all_prices())
c.set_default_price(5000)
print(c.print_all_prices())
