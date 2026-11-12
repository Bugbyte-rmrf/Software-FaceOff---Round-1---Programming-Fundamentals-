class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")


car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

car1.drive()
car2.drive()

#Encapsulation
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance


account = BankAccount(100)

account.deposit(50)

print(account.get_balance())

#Inheritance
class Animal:
    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def bark(self):
        print("Woof!")


dog = Dog()

dog.speak()
dog.bark()

#Polymorphism
class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

#Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process(self):
        pass


class CardPayment(Payment):

    def process(self):
        print("Processing card payment.")


payment = CardPayment()
payment.process()

#Overriding Method
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


dog = Dog()
dog.speak()

#Overloading method
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


calculator = Calculator()

print(calculator.add(2, 3))
print(calculator.add(2, 3, 4))

