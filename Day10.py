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