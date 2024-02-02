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

class OnlineStore(Subject):
    def __init__(self, name):
        super().__init__() 
        self.name = name 
        self.products = {} 

    def add_product(self, name, price):
        self.products[name] = price

    def change_price(self, name, price):
        self.products[name] = price
        self.notify()

class Observer:
    def update(self, subject):
        pass

class Customer(Observer):
    def __init__(self, name):
        self.name = name 
        self.interests = []

    def add_interest(self, product):
        self.interests.append(product)

    def update(self, subject):
        for product in self.interests:
            if product in subject.products:
                print(f"Olá, {self.name}. O produto {product} da loja {subject.name} mudou de preço. O novo preço é R$ {subject.products[product]:.2f}.")

store = OnlineStore("Loja do Nunca")

joao = Customer("Joao")
bob = Customer("Bob")

store.add_product("Livro", 50.00)
store.add_product("Celular", 1000.00)
store.add_product("Notebook", 2000.00)

joao.add_interest("Livro")
joao.add_interest("Notebook")
bob.add_interest("Celular")

store.attach(joao)
store.attach(bob)

store.change_price("Livro", 40.00)
store.change_price("Celular", 900.00)
