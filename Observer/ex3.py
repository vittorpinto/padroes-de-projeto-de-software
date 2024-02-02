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

class ClickCounter(Subject):
    def __init__(self):
        super().__init__()
        self.clicks = 0

    def click(self):
        self.clicks += 1
        self.notify()

class ClickPrinter(Observer):
    def update(self, subject):
        print(f"O número de cliques é {subject.clicks}")

class ClickLogger(Observer):
    def update(self, subject):
        with open("clicks.txt", "a") as file:
            file.write(f"O número de cliques é {subject.clicks}\n")

counter = ClickCounter()
printer = ClickPrinter()
logger = ClickLogger()

counter.attach(printer)
counter.attach(logger)

counter.click()
counter.click()
counter.click()
