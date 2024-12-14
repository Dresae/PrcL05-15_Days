"""Day 8 Object Oriented Programming(OOP)
==========================
1. Create a class to represent a Student with attributes such as name, age, and grade.
2. Given a csv file with employee details (name, position,salary), create a class to represent an employee.
3. Implement a program that simulates a basic bank account using a BankAccount class.
4. Write a python program that uses a rectangle class to calculate the area and perimeter of a rectangle.
5.Create a class to represent a car with attributes such as make, model, and year.
6. Given a json file with customer data, create a customer class to store and manipulate the data.
7. Write a prgram that that uses a Person class to track of a person's name, age and address.
8. Implement a program that uses a circle class to calculate the area and circumference of a circle.
9. Given a csv file with product details (name, price, quantity), create a class to manage the data.
10. Create a class to represent a movie with attributes such as title, director, and rating.
11. Create a class to represent a basic  calculator with add, substract, multiply and divide methods.
12 Create a class to represent a book with attributes such as title, author, and publication year.

"""

# -------------------------------------------------------------------  
# 1. Create a class to represent a Student with attributes such as name, age, and grade
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name    
    