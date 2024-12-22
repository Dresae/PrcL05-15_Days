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
9. Given a csv file with employee details(name, position, salary), create an employee class with private atttributes
10. Implement a program  that uses inheritance to represent a hierarchy pf shapes(circle, triangle, rectangle)
11. Create a base class Animal with a method sound() and create derived classes Dog and Cat with their own sound().
12. Implement a class hierarchy to represent different types of vehicles(car, bike) with their own attributes and methods
13. Create a class Person with private attributes and define methods to get and set the values of those attributes. 

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


