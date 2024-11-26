"""Day 1 Challenge - Content
================================
1. Calculate the area of a rectangle given its length and width
2. Take the user's name and age as input and print a greeting message
3. Check if a number is even or odd
4. Given a list of numbers, find the max and min
5. Create a function that check if given string is a palindrome
6. Calculate the compound interest for a given principal, interest rate, and time period
7. Converts a given numbers of days  into years, weeeks and days
8. Given a list of integers, find the sum of all positive numbers
8. Given a list of integers, find the sum of all positive numbers
9. Create a program that takes a sentence as input and counts the number of words in the sentence
10. Implement a program that swaps the values of two variables 
"""

# -------------------------------------------------------------------
# 1. Calculate the area of a rectangle given its length and width

length = float(input("Enter the length of the rectangle in meters: "))
width = float(input("Enter the width of the rectangle in meters: "))
area = length * width
print("The area of the rectangle is:", area, "m²")


# -------------------------------------------------------------------
# 2. Take the user's name and age as input and print a greeting message

name = input("Enter your name: ")
print("Welcome to the park,", name)


# -------------------------------------------------------------------
# 3. Check if a number is even or odd

num = int(input("Enter a number: "))
mod = num % 2
if mod == 0:
    print(num, "is even")
else:
    print(num, "is odd")