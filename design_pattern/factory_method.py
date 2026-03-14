'''
Definition
Define a method for creating an object,
but it lets subclasses decide which class to instantiate

Advantage: Loos Coupling, Extensibility
Disadvantage:
Let’s consider a scenario where we create a set of vehicles,
and we use the Factory Method to create different types of vehicles
(e.g., Car, Truck, Motorcycle).
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Creator(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

class Car(Vehicle):
    def drive(self):
        print("driving car now")

class Truck(Vehicle):
    def drive(self):
        print("driving truck now")

class CarCreator(Creator):
    def create_vehicle(self) -> Vehicle:
        return Car()

class TruckCreator(Creator):
    def create_vehicle(self) -> Vehicle:
        return Truck()

# client code
def get_and_drive(creator):
    vehicle = creator.create_vehicle()
    vehicle.drive()

if __name__ == "__main__":
    get_and_drive(CarCreator())
    get_and_drive(TruckCreator())