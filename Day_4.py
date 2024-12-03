"""Day 3 Challenge - Function
==========================
1. Given a list of numbers, create a function to find the sum of all positive numbers
2. Write a Python function that checks if a given string is a palindrome
3. Implemenet a function to calculate the factorial of a number using recursion
4. Create a function that finds the square of each element in a given list
5. Write a function that checks if a number is even or odd and return "Even" or "Odd" accordingly.
6. Calculate the area of a triangle given its base and height using a function
7. Create a function that takes a list of strings and returns the list sorted alphabetically
8. Write a function that takes two lists and return their intersection(common elements)
9. Implement a function that checks if a given year is leap or not
10. Create a function that takes a number as inut and prints its multiplication table
11. Write a function to calculate the area of a circle given its radius
12. Create a function to check if a given number is prime
13. Implement a function that reverses a given string

"""

# -------------------------------------------------------------------
# 1. Given a list of numbers, create a function to find the sum of all positive numbers
numbers = [13, -64, 24, 10, 74, -97, 50, -52, 13, 24, 68, -85, 61, 69, -45, 43, 20, 90, 83, 4]
def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

sum_positive_numbers(numbers)


# -------------------------------------------------------------------
# 2. Write a Python function that checks if a given string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

is_palindrome("racecar")

# -------------------------------------------------------------------
# 3. Implemenet a function to calculate the factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 

factorial(5)

# -------------------------------------------------------------------
# 4. Create a function that finds the square of each element in a given list
numbers = [2, 3, 4, 5]
def square_list(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

square_list(numbers)

# -------------------------------------------------------------------
# 5. Write a function that checks if a number is even or odd and return "Even" or "Odd" accordingly.
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

check_even_odd(4)