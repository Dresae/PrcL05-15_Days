"""Day 8 Object Oriented Programming(OOP)
==========================
1. Create a class to represent a Student with attributes such as Name, age, and grade.
2. Given a csv file with employee details (Name, Id, Profession ,Salary), create a class to represent an employee
3. Implement a program that simulates a basic bank account using a BankAccount class.
4. Write a python program that uses a rectangle class to calculate the area and perimeter of a rectangle.
5.Create a class to represent a car with attributes such as make, model, and year.
6. Given a json file with customer data, create a customer class to store and manipulate the data.
7. Write a prgram that that uses a Person class to track of a person's Name, age and address.
8. Implement a program that uses a circle class to calculate the area and circumference of a circle.
9. Given a csv file with product details (Name, price, quantity), create a class to manage the data.
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