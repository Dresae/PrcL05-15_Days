"""Day 9     Object Oriented Programming(OOP)
==========================
1. Create a class to represent a Student with attributes such as Name, age, and grade.
2. Given a csv file with employee details (Name, Id, Profession ,Salary), create a class to represent an employee
3. Implement a program that simulates a basic bank account using a BankAccount class.
4. Write a python program that uses a rectangle class to calculate the area and perimeter of a rectangle.
5.Create a class to represent a car with attributes such as make, model, and year.
6. Given a json file with customer data, create a customer class to store and manipulate the data.
7. Write a prgram that that uses a Person class to track of a person's Name, age and address.
8. Implement a program that uses a circle class to calculate the area and circumference of a circle.
9. Given a csv file with product details (Name, Price, Quantity), create a class to manage the data.
10. Create a class to represent a movie with attributes such as title, director, and rating.
11. Create a class to represent a basic  calculator with add, substract, multiply and divide methods.
12 Create a class to represent a book with attributes such as title, author, and publication year.

"""

# -------------------------------------------------------------------  
'''
# 1. Create a class to represent a Student with attributes such as Name, age, and grade
class Student:
    def __init__(self, Name, age, grade):
        self.Name = Name
        self.age = age
        self.grade = grade

student1 = Student("John", 15, "A")
student2 = Student("Jane", 16, "B")

print(student1.Name)
'''
# -------------------------------------------------------------------
'''
# 2. Given a csv file with employee details (Name, Id, Profession ,Salary), create a class to represent an employee
import os
import csv
import pandas as pd

dir_path = 'sample'
file_name = 'employees_info.csv' #Located at 'sample' folder
abs_path = os.path.join(dir_path, file_name)
df = pd.read_csv(abs_path)

#  Create a class to represent an employee
class Employee:
    def __init__(self, Name, ID, Profession, Salary):
        self.Name = Name
        self.ID = ID
        self.Profession = Profession
        self.Salary = Salary

    def __str__(self):
        return f"{self.Name}, {self.ID}, {self.Profession}, {self.Salary}"
    
with open(abs_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    employees = []

    # Create an Employee object for each row in the CSV
    for row in reader:
        employee = Employee(
            row['Name'],
            row['ID'],
            row['Profession'],
            row['Salary']
        )
        employees.append(employee)

print(employees[8]) # print a single object through its index
'''
# -------------------------------------------------------------------
'''
# 3. Implement a program that simulates a basic bank account using a BankAccount class.
class BankAccount:
    def __init__(self, balance):
        
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance
    

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
'''
# -------------------------------------------------------------------
'''
# 4. Write a python program that uses a rectangle class to calculate the area and perimeter of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(5, 3)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
'''
# -------------------------------------------------------------------
'''
# 5. Create a class to represent a car with attributes such as make, model, and year.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Ford", "Mustang", 2021)
print(car1.make)
print(car2.make)
print(car3.make)
'''

# -------------------------------------------------------------------
'''
# 6. Given a json file with customer data, create a customer class to store and manipulate the data
import os
import json
import pandas as pd

dir_path = 'sample'
file_name = 'customer_data.json' #Located at 'sample' folder
abs_path = os.path.join(dir_path, file_name)

with open(abs_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# class definition
class Customer:
    def __init__(self, firstName, lastName, age, address, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.address = address
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"{self.firstName}, {self.lastName}, {self.age}, {self.address}, {self.phoneNumber}"
    
with open(abs_path, 'r') as f:
    data = json.load(f)

customers = []

for customer_data in data:
    customer = Customer(
        customer_data['firstName'],
        customer_data['lastName'],
        customer_data['age'],
        customer_data['address'],
        customer_data['phoneNumber']
    )
    customers.append(customer)

print(customers[5])
'''

# -------------------------------------------------------------------
'''
# 7. Create a class to represent a student with attributes such as Name, age, and grade.
class Student:
    def __init__(self, Name, age, grade):
        self.Name = Name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.Name}, {self.age}, {self.grade}"
    
student1 = Student("Alice", 15, "A")
student2 = Student("Bob", 16, "B")
student3 = Student("Charlie", 14, "C")
print(student1)
print(student2)
print(student3)
'''

# -------------------------------------------------------------------
'''
# 8. Implement a program that uses a circle class to calculate the area and circumference of a circle
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
'''

# -------------------------------------------------------------------
'''
# 9. Given a csv file with product details (Name, Price, Quantity), create a class to manage the data
import os
import csv
import pandas as pd

dir_path = 'sample'
file_name = 'products.csv' #Located at 'sample' folder
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)

# class definition
class Product:
    def __init__(self, Name, Price, Quantity, Provider):
        self.Name = Name
        self.Price = Price
        self.Quantity = Quantity
        self.Provider = Provider

    def __str__(self):
        return f"{self.Name}, {self.Price}, {self.Quantity}, {self.Provider}"
    
products = []

for product_data in df.values:
    product = Product(
        product_data[0],
        product_data[1],
        product_data[2],
        product_data[3]
    )
    products.append(product)

print(products[6])
'''

# -------------------------------------------------------------------
'''
# 10. Create a class to represent a movie with attributes such as title, director, and rating.
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __str__(self):
        return f"{self.title}, {self.director}, {self.rating}"
    
movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 9.3)
movie2 = Movie("The Godfather", "Francis Ford Coppola", 9.2)
movie3 = Movie("The Dark Knight", "Christopher Nolan", 9.0)
print(movie1)
print(movie2)
print(movie3)
'''

# -------------------------------------------------------------------
'''
# 11. Create a class to represent a basic  calculator with add, substract, multiply and divide methods.
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

calculator = Calculator(10, 5)
print(calculator.add())
print(calculator.subtract())
print(calculator.multiply())
print(calculator.divide())
'''

# -------------------------------------------------------------------
'''
# 12. Create a class to represent a book with attributes such as title, author, and publication year.
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.publication_year}"
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print(book1)
print(book2)
'''
