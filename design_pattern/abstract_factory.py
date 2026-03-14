'''
Definition:
Create a set of families of related objects without specifying their concrete classes

Advantage:
Decouple object creation from the system that uses these objects
Consistency within the same families. Working well with others by following the same rules
Flexibility and Extensibility

Disadvantage:
Difficult to change the interface. Need to reimplement for all concrete classes
Rigid class structure. Factory is fixed with the combination of the products.

Example:
Imagine you're building a GUI framework that should support multiple themes: DarkTheme, LightTheme, etc.

You want to generate themed components like Button, Checkbox, Textbox, etc., without hardcoding which theme is being used.
'''

from abc import ABC, abstractmethod

# abstract class for button
class Button(ABC):
    @abstractmethod # declare this is an abstract method, must be defined for child classes
    def render(self):
        pass

# abtract class for button
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

class DarkButton(Button):
    def render(self):
        self.theme = "dark"
        print("Rendering dark theme")

class LightButton(Button):
    def render(self):
        self.theme = "light"
        print("Rendering light theme")

class DarkCheckbox(Checkbox):
    def render(self):
        print("Rendering dark checkbox")

class LightCheckbox(Checkbox):
    def render(self):
        print("Rendering light checkbox")

# Core: The interface interacting with clients
class Factory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_box(self):
        pass

class DarkFactory(Factory):
    def create_button(self):
        return DarkButton()

    def create_box(self):
        return DarkCheckbox()

class LightFactory(Factory):
    def create_button(self):
        return LightButton()

    def create_box(self):
        return LightCheckbox()
# client code
def render_ui(factory):
    button = factory.create_button()
    box = factory.create_box()
    button.render()
    box.render()


if __name__=="__main__":
    render_ui(DarkFactory())
    render_ui(LightFactory())


