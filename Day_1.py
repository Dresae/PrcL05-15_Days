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


# -------------------------------------------------------------------
# 4. Given a list of numbers, find the max and min values in the list.

numbers = [13, 64, 24, 10, 74, 97, 50, 52, 13, 24, 68, 85, 61, 69, 45, 43, 20, 90, 83, 4]

max_value = max(numbers)
min_value = min(numbers)

print("The maximum value in the list is:", max_value)
print("The minimum value in the list is:", min_value)


# -------------------------------------------------------------------
# 5. Create a function that check if given string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# -------------------------------------------------------------------
# 6. Calculate the compound interest for a given principal, interest rate, and time period

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

compound_interest = principal * (1 + rate / 100) ** time

print(f"The compound interest is: {compound_interest}")
print("The compound interest is: $" + str(round(compound_interest,3)))


# -------------------------------------------------------------------
# 7. Converts a given numbers of days  into years, weeks and days
days = int(input("Enter the number of days: "))

years = days // 365
weeks = (days % 365) // 7   
days = (days % 365) % 7

print(f"Years calculated: {years}" + "\n" + f"Weeks calculated: {weeks}" + "\n" + f"Days calculated: {days}")


# -------------------------------------------------------------------
# 8. Given a list of integers, find the sum of all positive numbers

numbers = [13, 64, 24, 10, 74, 97, 50, 52, 13, 24, 68, 85, 61, 69, 45, 43, 20, 90, 83, 4]

positive_sum = sum([x for x in numbers if x > 0])
print("The sum of all positive numbers in the list is:", positive_sum)


# -------------------------------------------------------------------
# 9. Create a program that takes a sentence as input and counts the number of words in the sentence

sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print("The number of words in the sentence is:", word_count)


# -------------------------------------------------------------------
# 10. Implement a program that swaps the values of two variables 
