"""Day 6 List and Tuples
==========================
1. Given two lists of numbers, concatenate them into a single list
2. Write a program that finds the largest and smallest number in a list
3. Implement a function that takes a list of numbers and returns a new list with squared values
4. Create a program that finds the common elements between two lists and store themm into a new list
5. Given a list of words, find a word with the maximun length and its length
6. Write a Python program to count the occurrences of each element in a given list
7. Given a list of names, remove all duplicate names and print the unique names
8. Create a function that takes a lists of strings and returns the list sorted by the of the strings
9. Write a program that checks if a given list is sorted in ascending order
10. Implement a function that takes two lists and returns their union (all unique elements from both lists)
11. Given a list of numbers, find the sum and average using built-in functions
12. Create a list of fruits and add a new fruit to the list
13. Access elements in a tuple using indexing.

"""

# -------------------------------------------------------------------
# 1. Given two lists of numbers, concatenate them into a single list

list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2
print(concatenated_list)

# -------------------------------------------------------------------
# 2. Write a program that finds the largest and smallest number in a list

numbers = [13, 64, 24, 10, 74, 97, 50, 52, 13, 24, 68, 85, 61, 69, 45, 43, 20, 90, 83, 4]
largest = max(numbers)
smallest = min(numbers)

print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

# -------------------------------------------------------------------
# 3. Implement a function that takes a list of numbers and returns a new list with squared values

numbers = [1, 2, 3, 4, 5]

def square_list(numbers):
    squared = [] # empty list to store the new values
    for num in numbers:
        squared.append(num ** 2) # .append method is used tto add new values to the empty list
    return squared

print(square_list(numbers))

# -------------------------------------------------------------------
# 4. Create a program that finds the common elements between two lists and store them into a new list  
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = [value for value in list1 if value in list2] # This list comprehension check for common elements
print(common_elements)

# -------------------------------------------------------------------
# 5. Given a list of words, find a word with the maximun length and its length

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

max_length = 0 # this variable is used to  initialize the loop
max_word = ""

for word in words:
    if len(word) > max_length: # here the loop iterate over each word in the list until it stops when finding the one with maximun lenght
        max_length = len(word) # the variable value is update on each loop iteration
        max_word = word

print("The word with the maximum length is:", max_word)
print("The length of the word is:", max_length)