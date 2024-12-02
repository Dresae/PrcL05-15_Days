"""Day 3 Challenge - Content Control Flow and Loops
==========================
1. Write a program that takes a number as input and checks if it is positive, negative, or zero.
2. Create a loop that prints the first 10 even numbers
3. Implement a  program that finds the largest and smallest number in a list of integers
4. Write a program that checks if a given year is a leap year or not
5. Given a list of integers, find all the even numbers  and store them in a new list
6.Write a program that check if a given number is prime
7. Create a program that generates the Fibonacci sequence up to a given number of terms
8. Given a list of names, print all the names starting with the letter 'A'
9. Implement a program that prints the multiplication table of a given number
10. Write a program that calculates the factorial of a given number
11. Create a loop that prints all the prime numbers between 1 anf 100
12. Given a list of words, count the number of words with more than 5 characters
13. Calculate the sum of digits of a given number
"""

# -------------------------------------------------------------------
# 1. Write a program that takes a number as input and checks if it is positive, negative, or zero.

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# -------------------------------------------------------------------
# 2. Create a loop that prints the first 10 even numbers

for num in range(2, 21, 2):
    print(num)


# -------------------------------------------------------------------
# 3. Implement a  program that finds the largest and smallest number in a list of integers

numbers = [13, 64, 24, 10, 74, 97, 50, 52, 13, 24, 68, 85, 61, 69, 45, 43, 20, 90, 83, 4]
largest = max(numbers)
smallest = min(numbers)

print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)


# -------------------------------------------------------------------
# 4. Write a program that checks if a given year is a leap year or not

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# -------------------------------------------------------------------
# 5. Given a list of integers, find all the even numbers  and store them in a new list

numbers = [13, 64, 24, 10, 74, 97, 50, 52, 13, 24, 68, 85, 61, 69, 45, 43, 20, 90, 83, 4]
even_numbers = [num for num in numbers if num % 2 == 0]
print("The even numbers in the list are:", even_numbers)

# -------------------------------------------------------------------
# 6. Write a program that check if a given number is prime

number = int(input("Enter a number: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

# -------------------------------------------------------------------
# 7. Create a program that generates the Fibonacci sequence up to a given number of terms

terms = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(terms):
    print(a)
    a, b = b, a + b


# -------------------------------------------------------------------
# 8. Given a list of names, print all the names starting with the letter 'A'

names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Anne", "Grace", "Hannah", "Isabella", "Jack"]
for name in names:
    if name.startswith("A"):
        print(name)