"""Day 2 Challenge - Content
================================
1. Given a list of numbers, find the sum and average.
2. Create a program that takes a temperature in Farenheit and converts it tp celsius
3. Implement a program that checks if a given string is a palindrome
4. Create a funtion that reverse a given string
5. Given a list of names, concatenate them into a single string separated by dashes
6. Write a Python program that check if a given string is a pangram(contains  all letter of the alphabet)
7. calculate the area and circle given its radius
8. Implement a program that converts a given number of minutes into hours and minutes
9. Create a function to to count the number of vowels in a given string
10. Write a program to check if a number is prime
"""

# -------------------------------------------------------------------
# 1. Given a list of numbers, find the sum and average.

import random
# generate 10 random integers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]  
print("List generated: ", random_list)

num_count = len([x for x in random_list if isinstance(x, int)])
result = sum(random_list)/num_count

print("Average =", result)


# -------------------------------------------------------------------
# 2. Create a program that takes a temperature in Farenheit and converts it tp celsius

converter = print("TEMPERATURE CONVERTER")
value = float(input("Enter a temperature value in Farenheit: "))
# Formula for conversion: C = (°F - 32) × 5/9
convert = round((value - 32) * (5/9), 2)

print(convert, "C°")


# -------------------------------------------------------------------
# 3. Implement a program that checks if a given string is a palindrome

def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# -------------------------------------------------------------------
# 4. Create a funtion that reverse a given string

string = input("Enter a word you want to reverese: ")
print(string[::-1])


# -------------------------------------------------------------------
# 5. Given a list of names, concatenate them into a single string separated by dashes

names = ['Mariah', 'Louise', 'Elvis', 'Carolina', 'Michael']
print("-".join(names))


# -------------------------------------------------------------------
# 6. Write a Python program that check if a given string is a pangram(contains  all letter of the alphabet)
import string

# Lets create the function that will perform the task
def is_pangram(sentence):
    # convert the given to lowercase.
    sentence = sentence.lower()
    # remove the spaces from the sentence
    sentence = sentence.replace(' ', '')

    # Create a set of all letters of the alphabet
    alphabet = set(string.ascii_lowercase)
    # Create a set with the letters of the given sentence
    input_set = set(sentence)

    # Check if all letters in the alphabet are presetnt in the sentence
    return alphabet.issubset(input_set)

# Use case
input_string = input("Enter a sentence: ")
if is_pangram(input_string):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")



# -------------------------------------------------------------------
# 7. calculate the area and circle given its radius
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print("The area of the circle is:", area)

# -------------------------------------------------------------------
# 8. Implement a program that converts a given number of minutes into hours and minutes
minutes = int(input("Enter the number of minutes: "))
hours = minutes // 60
minutes = minutes % 60
print(f"{hours} hours and {minutes} minutes")

# -------------------------------------------------------------------
# 9. Create a function to count the number of vowels in a input string
def count_vowels(string):
    count = 0
    for char in string:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

input_string = input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowels(input_string)}")

# -------------------------------------------------------------------
# 10. Write a program to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# -------------------------------------------------------------------



