"""Day 8 File Handling
==========================
1. Write a python program to copy the contents of one text file into another.
2. Given a CSV file with students names and scores, find the student with the highest score.
3. Implement a program that reads a text file and counts the number of words and lines in it.
4. Create a function that takes a list of sentences and writes them to a text file, each on a new line.
5. Given a CSV file with employee details(name, age salary), calculate the average salary of all employees.
6. Write a program that reads a CSV file a and finds the total sales revenue for a specific product.
7. Given a text file with a list of numbers, write a function that find the sum of all numbers in the file.
8. Implement a program that reads a CSV file and generates a bar chart that reperesents the data using Matplotlib.
9. Write a function that reads a JSON fileand extracts especific information from it.
10. Given a CSV file with temperature data for each day of the weak, find the average temperature for each day.
11. Write a program that reads a text file and prints its content.
12. Create a new text file and write some content into it.
13. Implement a program that reads a CSV file and generates a scatter plot that reperesents the data using Matplotlib.

"""
# -------------------------------------------------------------------
# 1. Write a python program to copy the contents of one text file into another 
import os
import pandas as pd

# Define the data directory relative to the current script location
dir_path = 'sample'
file_name1 = 'file1.txt'
file_name2 = 'file2.txt'

abs_path1 = os.path.join(dir_path, file_name1) # absolute path for file 1
abs_path2 = os.path.join(dir_path, file_name2) # absolute path for file 2

df = pd.read_csv(abs_path1)
df.to_csv(abs_path2, index=False) # copying the file content into the file2.txt