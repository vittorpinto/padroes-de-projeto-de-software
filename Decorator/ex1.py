class Hamburger:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class SimpleHamburger(Hamburger):
    def __init__(self):
        super().__init__("Hambúrguer Simples", 10.00) 

class HamburgerDecorator(Hamburger):
    def __init__(self, hamburger):
        self.hamburger = hamburger 

    def get_name(self):
        return self.hamburger.get_name()

    def get_price(self):
        return self.hamburger.get_price()

class CheeseDecorator(HamburgerDecorator):
    def __init__(self, hamburger):
        super().__init__(hamburger) 

    def get_name(self):
        return self.hamburger.get_name() + " com Queijo"

    def get_price(self):
        return self.hamburger.get_price() + 2.00

class BaconDecorator(HamburgerDecorator):
    def __init__(self, hamburger):
        super().__init__(hamburger) 

    def get_name(self):
        return self.hamburger.get_name() + " com Bacon"

    def get_price(self):
        return self.hamburger.get_price() + 3.00

class LettuceDecorator(HamburgerDecorator):
    def __init__(self, hamburger):
        super().__init__(hamburger) 

    def get_name(self):
        return self.hamburger.get_name() + " com Alface"

    def get_price(self):
        return self.hamburger.get_price() + 1.00

class TomatoDecorator(HamburgerDecorator):
    def __init__(self, hamburger):
        super().__init__(hamburger) 

    def get_name(self):
        return self.hamburger.get_name() + " com Tomate"

    def get_price(self):
        return self.hamburger.get_price() + 1.50

hamburger = SimpleHamburger()

hamburger = CheeseDecorator(hamburger)
hamburger = BaconDecorator(hamburger)

print(f"{hamburger.get_name()}: R$ {hamburger.get_price():.2f}")