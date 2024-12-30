"""Day 11 Introduction to Numpy for Numerical Computing
==========================
1. Given a list of numbers, create a Numpy array and find the sum and products of its elements
2. Implement a program that generates a Numpy array and reshapes it into a shape of 3x3 matrix
3. Write a python program that uses NumPy to find the mean, median and standard deviation of a given dataset
4. Create a function that takes a list of numbers and returns a NumPy array and sort it in ascending order
5. Given a list of lists, create a 2D NumPy array and find the sum of elements in each row and column
6. Implement a program that generates a NumPy array and finds the maximun and minimum value
7. Write a function that takes a Numpy array and returns a new array with all elements squared
8. Given a Numpy array, calculate the dot product with the array with itself
9. Create a program that uses Numpy to calculate the inverse of a 2X2 matrix
10. Implement a function that takes a Numpy array and returns the transpose of the array 
11. Create a Numpy array for a python list and perform basic operations like addition, subtraction, multiplication and division
12. Generate a Numpy array with random numbers and calculate its mean, median and standard deviation
13. Create a Numpy array and reshape it into a different shape  

"""

# -------------------------------------------------------------------
"""
# 1. Given a list of numbers, create a Numpy array and find the sum and products of its elements
import numpy as np
list_1 = [1.25, 2.34, 3.45, 4.56, 5.54, 6.77, 7.89, 8.62, 9.59, 10.32]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_1_array = np.array(list_1) # convert the list into a numpy array using the 'np.array()' method
list_2_array = np.array(list_2)

sum_1 = np.round(list_1_array.sum(), decimals=2)    # the 'sum()' method is used to calculate the sum of its elements
product_1 = np.round(list_1_array.prod(), decimals=2) # using round method to round off the decimals

sum_2 = list_2_array.sum()
product_2 = list_2_array.prod()


print("The sum of list1 is:", sum_1)
print("The product of list1 is:", product_1, "\n")
print("The sum of list2 is:", sum_2)
print("The product of list2 is:", product_2)
"""

# -------------------------------------------------------------------
# 2. Implement a program that generates a Numpy array and reshapes it into a shape of 3x3 matrix
"""
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped_array = array.reshape(3, 3)
print(reshaped_array)
"""

# -------------------------------------------------------------------

# 3. Write a python program that uses NumPy to find the mean, median and standard deviation of a given dataset
"""
import numpy as np
dataset = [1.25, 2.845, 3.546, 4.221, 5.75, 6.36, 7.64, 8, 9.89, 10]
 
data_mean = np.round(np.mean(dataset), decimals=3) 
data_median = np.round(np.median(dataset), decimals=3) 
data_std = np.round(np.std(dataset), decimals=3)     

print("The mean of the dataset is:", data_mean)
print("The median of the dataset is:", data_median)
print("The standard deviation of the dataset is:", data_std)
"""

# -------------------------------------------------------------------

# 4. Create a function that takes a list of numbers and returns a NumPy array and sort it in ascending order
"""
import numpy as np
list_1 = [325, 5421, 6589, 758, 258, 2368, 456, 789, 123, 4567]
list_1_array = np.sort(np.array(list_1))

print("The sorted array is:", list_1_array)
"""
# -------------------------------------------------------------------

# 5. Given a list of lists, create a 2D NumPy array and find the sum of elements in each row and column
"""
import numpy as np
list_1 = [[135, 82, 215], [54, 32, 548], [59, 25, 932], [65, 32, 456], [12, 23, 45]]
list_1_array = np.array(list_1)

print("The 2D array is:", "\n", list_1_array, "\n")

print("The sum of elements in each column is:", list_1_array.sum(axis=0)) # axis=0 is used for operations with columns
print("The sum of elements in each row is:", list_1_array.sum(axis=1))
"""
# -------------------------------------------------------------------

# 6. Implement a program that generates a NumPy array and finds the maximun and minimum value
"""
import numpy as np
my_array = np.array([135, 82, 215, 54, 32, 548, 59, 25, 932, 65, 32, 456, 12, 23, 45])
max_value = np.max(my_array)
min_value = np.min(my_array)

print("The maximum value is:", max_value)
print("The minimum value is:", min_value)
"""

# -------------------------------------------------------------------

# 7. Write a function that takes a Numpy array and returns a new array with all elements squared
"""
import numpy as np
my_array = np.array([3, 4, 5, 6, 7, 8, 9])
squared_array = my_array**2

print("Original array is:", my_array)
print("Squared array is:", squared_array)
"""
# -------------------------------------------------------------------

# 8. Given a Numpy array, calculate the dot product with the array with itself

import numpy as np
my_array = np.array([3, 4, 5, 6, 7, 8, 9])
dot_product = np.dot(my_array, my_array)

print("The dot product is:", dot_product)
