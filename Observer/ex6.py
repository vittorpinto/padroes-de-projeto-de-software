class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class StockManager(Subject):
    def __init__(self):
        super().__init__()
        self.products = {}

    def update_stock(self, product, quantity):
        if product not in self.products or quantity != self.products[product]:
            self.products[product] = quantity
            self.notify()

class StockDisplay(Observer):
    def update(self, subject):
        print(f"O estoque atual é: {subject.products}")

class StockAlert(Observer):
    def __init__(self, limit):
        self.limit = limit

    def update(self, subject):
        for product, quantity in subject.products.items():
            if quantity < self.limit:
                print(f"ALERTA! O produto {product} está com o estoque baixo: {quantity}")

manager = StockManager()
display = StockDisplay()
alert = StockAlert(10)

manager.attach(display)
manager.attach(alert)

manager.update_stock("manete", 20)
manager.update_stock("mouse", 15)
manager.update_stock("monitor", 8)
manager.update_stock("cpu", 5)
manager.update_stock("monitor", 12)
