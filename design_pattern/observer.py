'''
Definition
One-to-many dependency between objects
When one object changes state, all its dependents are notified and updated automatically
"Publish-Subscribe": event-driven programming

Example:
    Let’s model a weather station (subject) that notifies multiple display elements (observers) when the temperature changes.
'''

from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Subject (Observable) Interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"[WeatherStation] New temperature: {temperature}°C")
        self._temperature = temperature
        self.notify()

# Concrete Observers
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"[PhoneDisplay] Temperature updated to {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature):
        print(f"[WindowDisplay] It's now {temperature}°C outside")

# Client code
if __name__ == "__main__":
    station = WeatherStation()
    phone = PhoneDisplay()
    window = WindowDisplay()

    station.attach(phone)
    station.attach(window)

    station.set_temperature(22)
    station.set_temperature(25)

    station.detach(phone)

    station.set_temperature(30)
