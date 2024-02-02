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

class ElectronicBallot(Subject):
    def __init__(self):
        super().__init__() 
        self.candidates = {} 

    def add_candidate(self, name):
        self.candidates[name] = 0

    def vote(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            self.notify()
        else:
            print(f"Candidato {name} não encontrado.")

class Observer:
    def update(self, subject):
        pass

class BallotBulletin(Observer):
    def update(self, subject):
        print(f"Boletim de urna atualizado:")
        for name, votes in subject.candidates.items():
            print(f"{name}: {votes} votos")

ballot = ElectronicBallot()

bulletin = BallotBulletin()

ballot.attach(bulletin)

ballot.add_candidate("Joao")
ballot.add_candidate("Vitor")
ballot.add_candidate("Antonio")

ballot.vote("Joao")
ballot.vote("Vitor")
ballot.vote("Joao")
ballot.vote("Antonio")
ballot.vote("Vitor")
ballot.vote("Vitor")
ballot.vote("Fulano")