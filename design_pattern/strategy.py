'''
Definition
Define a family of algorithms, encapsulate each one, and
make them interchangeable.
Decouple algo from clients

Example
An app can process payments using Credit Card, Paypal or Crypto
Swith them between runtime without changing the client code
'''

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def pay(self, amount):
        print(f"Pay ${amount} using Credit Card({self.card_number})")


class PaypalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email
    def pay(self, amount):
        print(f"Pay ${amount} using Paypal({self.email})")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentMethod):
        self.items = []
        self.payment_strategy = payment_strategy

    def add_item(self, item, price):
        self.items.append((item, price))

    def get_total(self):
        return sum(price for _, price in self.items)

    def checkout(self):
        total = self.get_total()
        print(f"Total: ${total}")
        self.payment_strategy.pay(total)
        self.items = []

    def set_payment_strategy(self, strategy: PaymentMethod):
        self.payment_strategy = strategy

# Client code
if __name__ == "__main__":
    cart = ShoppingCart(CreditCardPayment("1234-5678-9876-5432"))
    cart.add_item("Book", 12.99)
    cart.add_item("Pen", 2.50)
    cart.checkout()

    # Switch strategy at runtime
    cart.set_payment_strategy(PaypalPayment("user@example.com"))
    cart.add_item("Notebook", 5.75)
    cart.checkout()