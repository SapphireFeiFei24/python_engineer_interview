'''
Definition
Define the skeleton of an algorithm in an operation,
deferring some steps to subclasses.
Lets subclasses redefine certain steps of an algorithm without changing the algo's structure

Example
prepare a drink:
1. Boil water
2. Brew the drink (tea/coffee)
3. Pour in cup
4. Add condiments
'''

from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    # Skeleton of the algorithm
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring to cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

# Concrete class for Tea
class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

# Concrete class for Coffee
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")
# Client code
if __name__ == "__main__":
    print("Preparing tea:")
    tea = Tea()
    tea.prepare_recipe()

    print("\nPreparing coffee:")
    coffee = Coffee()
    coffee.prepare_recipe()