"""Day 10 Inheritance and Encapsulation
==========================
1. Create a base class my_shape with methods to calculate area and perimeter, and derive class Circle and Square.
2. Implement a class hierarchy to represent different types of employees(Manager, Engineer) with their attributes
3. Write a python program thet uses inheritance to represent a hierarchy of shapes(triangle, rectangle, etc)
4. Create a class hierarchy to reresent different types of animals(bird, fish) with their own attributes and methods
5. Given a Json file with product details(name, price, quantity), create a product class with encapsulated attributes
6. Implement a program that uses inheritance to represent a hierarchy of vehicles(car, bike, truck, etc)
7. Write a python program that uses encapsulation to protect sensitive information in a user class.
8. Create a class hierarchy to represent different types of electronics(phone, laptop) with their attributes
9. Create a class to represent a bank account with attributes such as account number, balance, and transaction history
10. Create a class to represent a student with attributes such as name, age, and grade
11. Implement a program that uses a circle class to calculate the area and circumference of a circle
12. Create a class Person with private attributes and define methods to get and set the values of those attributes. 

"""

# -------------------------------------------------------------------  
"""
# 1. Create a base class named my_sape with methods to calculate area and perimeter, and derive class Circle and Square.
import math

class my_shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass    

class Circle(my_shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * (self.radius ** 2), 2)
    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Square(my_shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return round(self.side ** 2, 2)
    def calculate_perimeter(self):
        return round(4 * self.side, 2)

circle = Circle(5.3)
square = Square(4.2)

print(circle.calculate_area()) 
print(circle.calculate_perimeter())  

print(square.calculate_area()) 
print(square.calculate_perimeter())  
"""

# -------------------------------------------------------------------
"""
# 2. Implement a class hierarchy to represent different types of employees(Manager, Engineer) with their attributes

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary    

class Manager(Employee):
    pass

class Engineer(Employee):
    pass
"""
# -------------------------------------------------------------------
"""
# 3. Write a python program thet uses inheritance to represent a hierarchy of shapes(triangle, rectangle, etc)
import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass    

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return round(math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2)
    def perimeter(self):
        return round(self.side1 + self.side2 + self.side3, 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return round(self.length * self.width, 2)
    def perimeter(self):
        return round(2 * (self.length + self.width), 2)

triangle = Triangle(3.6, 4, 5)
rectangle = Rectangle(6, 7.8)

print(triangle.area()) 
print(triangle.perimeter())  

print(rectangle.area()) 
print(rectangle.perimeter())

"""
# -------------------------------------------------------------------
"""
# 4. Create a class hierarchy to represent different types of animals(bird, fish) with their own attributes and methods

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def make_sound(self):
        return "Chirp chirp"

class Fish(Animal):
    def __init__(self, name, species, length):
        super().__init__(name, species)
        self.length = length

    def make_sound(self):
        return "Swish swish"    

bird = Bird("Tweety", "bird", 2.1)
fish = Fish("Nemo", "fish", 0.2)

print(bird.name) 
print(bird.species) 
print(bird.wingspan) 
print(bird.make_sound()) 

print(fish.name) 
print(fish.species) 
print(fish.length) 
print(fish.make_sound())

"""
# -------------------------------------------------------------------
"""
# 5. Given a Json file with product details(name, price, quantity), create a product class with encapsulated attributes

import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}"

with open("sample/products.json", "r") as file:
    data = json.load(file)
    products = []
    for product_data in data["fruits"]:
        product = Product(
            product_data["name"],
            product_data["price"],
            product_data["quantity"]
        )
        products.append(product)

    for product in products:
        print(product)
"""
# -------------------------------------------------------------------
"""
# 6. Implement a program that uses inheritance to represent a hierarchy of vehicles(car, bike, truck, etc)
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        pass
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.is_running = False

    def start(self):
        self.is_running = True
    def stop(self):
        self.is_running = False

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.is_running = False

    def start(self):
        self.is_running = True
    def stop(self):
        self.is_running = False

car = Car("Toyota", "Camry", 2022)
motorcycle = Motorcycle("Honda", "CBR", 2021)


car.start()
motorcycle.start()
print("Car running now? ", car.is_running)
print("Motorcycle running? ", motorcycle.is_running)
"""
# -------------------------------------------------------------------
"""
# 7. Write a python program that uses encapsulation to protect sensitive information in a user class.
class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

user = User("Alice", 25)
print(user.get_name()) 
print(user.get_age())

user.set_name("Bob")
user.set_age(30)

print(user.get_name()) 
print(user.get_age())
"""
# -------------------------------------------------------------------
"""
# 8. Create a class hierarchy to represent different types of electronics(phone, laptop) with their attributes
class Electronics:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.price = 0

    def set_price(self, price):
        self.price = price

class Phone(Electronics):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.screen_size = 0

    def set_screen_size(self, size):
        self.screen_size = size

class Laptop(Electronics):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.battery_life = 0

    def set_battery_life(self, life):
        self.battery_life = life

phone = Phone("Apple", "iPhone 12")
laptop = Laptop("Dell", "XPS 13")

phone.set_price(999)
phone.set_screen_size(6.1)

laptop.set_price(1499)
laptop.set_battery_life(7)

print("Phone: ", phone.brand, phone.model, phone.price, phone.screen_size)
print("Laptop: ", laptop.brand, laptop.model, laptop.price, laptop.battery_life)
"""

# -------------------------------------------------------------------
"""
# 9. Create a class to represent a bank account with attributes such as account number, balance, and transaction history
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        #return self.transaction_history
        print("\n".join(map(str, self.transaction_history)))


account = BankAccount("123456789", 1000)
account.deposit(500)
account.deposit(250)
account.withdraw(600)
account.deposit(620)
account.deposit(300)
account.deposit(250)
account.withdraw(150)
account.withdraw(200)

print("Your transactions history is: ", "\n")
print(account.get_transaction_history())
print("\n", "Your current balance is: ", "$", account.get_balance())
"""
# -------------------------------------------------------------------

"""
# 10. Create a class to represent a student with attributes such as name, age, and grade
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display_info(self): 
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    def update_grade(self, new_grade):
        self.grade = new_grade

student1 = Student("Alice", 15, "A")
student2 = Student("Bob", 16, "B")

student1.display_info()
student2.display_info()

student1.update_grade("B+")
student2.update_grade("A-")

student1.display_info()
student2.display_info()
"""


# -------------------------------------------------------------------
"""
# 11. Implement a program that uses a circle class to calculate the area and circumference of a circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)
    
circle = Circle(5)
print("Area:", circle.area())
print("Circumference:", circle.circumference())
"""
# -------------------------------------------------------------------
"""
# 12. Create a class Person with private attributes and define methods to get and set the values of those attributes. 
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

person = Person("Alice", 25)
print("Name:", person.get_name())
print("Age:", person.get_age())

person.set_name("Bob")
person.set_age(30)

print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())
"""
# -------------------------------------------------------------------