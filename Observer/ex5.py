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

class NewsPublisher(Subject):
    def __init__(self):
        super().__init__()
        self.news = None

    def publish(self, news):
        self.news = news
        self.notify()

class NewsReader(Observer):
    def update(self, subject):
        print(f"A nova notícia é: {subject.news}")

class NewsFilter(Observer):
    def __init__(self, criterion):
        self.criterion = criterion

    def update(self, subject):
        if self.criterion in subject.news:
            print(f"A nova notícia relevante é: {subject.news}")

publisher = NewsPublisher()
reader = NewsReader()
filter1 = NewsFilter("esporte")
filter2 = NewsFilter("política")

publisher.attach(reader)
publisher.attach(filter1)
publisher.attach(filter2)

publisher.publish("noticia!")
publisher.publish("noticia 2!")
publisher.publish("noticia 3!")
