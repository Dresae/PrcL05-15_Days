"""Day 7 Dictionaries and Sets
==========================
1. Given two dictionaries, merge them into a single dictionary
2. Write a program that finds the most frequent element in a list
3. implemenet a function that removes a key-value pair from a dictionary
4. Create a program that checks if two sets have elements in common
5. Given a list of dictionaries, find the dictionary with the highest value for a specific key
6. Write a Python program that count the number of ocurrences of each character on a given string using a dictionary
7. Given two sets, find the union, intersection, and difference between them
8. Create a function that takes a list of dictionaries and sort them based on a specific key
9. Write a program that finds the average value of all the elements in a list of dictionaries
10. Implement a function that takes a list of strings and returns a set of unique string present in all strings
11. Create a dictionary to store information about a person(name, age, city)
12. Add a new key-value pair to an existing dictionary
13. Create a set of unique numbers from a list of numbers

"""

# -------------------------------------------------------------------
# 1. Given two dictionaries, merge them into a single dictionary

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1.copy() # the .copy() method is used to create a copy of the dictionary
merged_dict.update(dict2) # the .update() method is used to add the key-value pairs from the second dictionary to the first dictionary
print(merged_dict)

# -------------------------------------------------------------------
# 2. Write a program that finds the most frequent element in a list

numbers = [1, 2, 3, 4, 1, 1, 2, 3, 4, 5, 1, 2, 3, 1, 5]
frequency = {} # empty dictionary to store the frequency of each number

for num in numbers:
    if num in frequency:
        frequency[num] += 1 # if the number is already in the dictionary it will add one to its count
    else:
        frequency[num] = 1 # if the number is not in the dictionary it will be added and set it counts to one '1'

max_count = max(frequency.values()) # the max() method is used to find the maximum value in the dictionary
most_frequent = [num for num, count in frequency.items() if count == max_count] # the list comprehension is used to find the keys that have the maximum value

print("The most frequent number(s) in the list are:", most_frequent)

# -------------------------------------------------------------------
# 3. Implement a function that removes a key-value pair from a dictionary

def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key] # the del keyword is used to delete the key-value pair from the dictionary
    return dictionary

dictionary = {"a": 1, "b": 2, "c": 3}
print(remove_key(dictionary, "b"))

# -------------------------------------------------------------------
# 4. Create a program that checks if two sets have elements in common

set1 = {1, 2, 3}
set2 = {3, 4, 5}

if set1.intersection(set2):
    print("The sets have common elements")
else:
    print("The sets have no common elements")

# -------------------------------------------------------------------
# 5. Given a list of dictionaries, find the dictionary with the highest value for a specific key
dicts = [{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]
key = "a"
max_value = max(dict[key] for dict in dicts) # the max() method is used to find the maximum value in the dictionary
max_dict = next(dict for dict in dicts if dict[key] == max_value) # the next() method is used to find the dictionary with the maximum value
print("The dictionary with the highest value for key", key, "is:", max_dict)

# -------------------------------------------------------------------
# 6. Write a Python program that count the number of ocurrences of each character on a given string using a dictionary
