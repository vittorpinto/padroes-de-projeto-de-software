from abc import ABC, abstractmethod
import logging

class Event(ABC):
    @abstractmethod
    def log(self, message):
        pass

class ErrorEvent(Event):
    def log(self, message):
        logging.error(message)

class WarningEvent(Event):
    def log(self, message):
        logging.warning(message)

class InfoEvent(Event):
    def log(self, message):
        logging.info(message)

class EventFactory(ABC):
    @abstractmethod
    def create_event(self, event_type):
        pass

class ConcreteEventFactory(EventFactory):
    def create_event(self, event_type):
        if event_type == "error":
            return ErrorEvent()
        elif event_type == "warning":
            return WarningEvent()
        elif event_type == "info":
            return InfoEvent()
        else:
            raise ValueError("Tipo de evento inválido")

def test_system(factory, event_type, message):
    event = factory.create_event(event_type)
    event.log(message)

print("Testando o sistema com diferentes tipos de eventos")
factory = ConcreteEventFactory()
event_types = ["error", "warning", "info"]
messages = ["Ocorreu um erro crítico", "Atenção: possível falha no sistema", "Operação realizada com sucesso"]
for event_type, message in zip(event_types, messages):
    test_system(factory, event_type, message)
