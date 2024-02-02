import datetime

class ChatSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class ChatObserver:
    def __init__(self, name):
        self._name = name

    def update(self, message):
        if self._name == message.sender or self._name == message.recipient:
            print(f"{self._name}: {message}")

class ChatMessage:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.time = datetime.datetime.now()

    def __str__(self):
        return f"De: {self.sender}\nPara: {self.recipient}\nConteúdo: {self.content}\nHorário: {self.time}"

chat = ChatSubject()

joao = ChatObserver("Joao")
vitor = ChatObserver("Vitor")
carol = ChatObserver("Carol")

chat.attach(joao)
chat.attach(vitor)
chat.attach(carol)

chat.notify(ChatMessage("Joao", "Vitor", "Olá, Vitor!"))
chat.notify(ChatMessage("Vitor", "Joao", "Olá, Joao!"))
chat.notify(ChatMessage("Carol", "Joao", "Oi, Joao!"))
chat.notify(ChatMessage("Joao", "Carol", "Oi, Carol!"))