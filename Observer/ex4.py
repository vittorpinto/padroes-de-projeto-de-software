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

class TemperatureSensor(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 0

    def set_temperature(self, value):
        if value != self.temperature:
            self.temperature = value
            self.notify()

class TemperatureDisplay(Observer):
    def update(self, subject):
        print(f"A temperatura atual é {subject.temperature}°C")

class TemperatureAlarm(Observer):
    def __init__(self, limit):
        self.limit = limit

    def update(self, subject):
        if subject.temperature > self.limit:
            print("A temperatura está muito alta")

sensor = TemperatureSensor()
display = TemperatureDisplay()
alarm = TemperatureAlarm(30)

sensor.attach(display)
sensor.attach(alarm)

sensor.set_temperature(25)
sensor.set_temperature(28)
sensor.set_temperature(31)
sensor.set_temperature(29)
