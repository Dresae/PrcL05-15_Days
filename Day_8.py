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
"""
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

"""
# -------------------------------------------------------------------
'''
# 2. Given a CSV file with students names and scores, find the student with the highest score   
import os
import pandas as pd

dir_path = 'sample'
file_name = 'students_scores.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
# max_value = df['Score'].max()
# max_value = df.nlargest(1, 'Name') 
max_score = df.loc[df['Score'].idxmax(), 'Name']
print(max_score)
'''
# -------------------------------------------------------------------
'''
# 3. Implement a program that reads a text file and counts the number of words and lines in it.
import os
import pandas as pd

dir_path = 'sample'
file_name = 'file2.txt'
abs_path = os.path.join(dir_path, file_name)

with open(abs_path, 'r') as f:
    content = f.read()
    words = len(content.split())
    lines = len(content.split('\n'))
    print(f"The file contains {words} words and {lines} lines.")
'''
# -------------------------------------------------------------------
'''
# 4. Create a function that takes a list of sentences and writes them to a text file, each on a new line.

def write_to_file(sentences):
    with open('sentences.txt', 'w') as f:
        for sentence in sentences:
            f.write(sentence + '\n')    
    print("Sentences written to file successfully.")
'''
# -------------------------------------------------------------------
'''
# 5. Given a CSV file with employee details(name, age salary), calculate the average salary of all employees.
import os
import pandas as pd

dir_path = 'sample'
file_name = 'employees_info.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
average_salary = df['Salary'].mean()
print(f"The average salary of all employees is: {average_salary}")
'''
# -------------------------------------------------------------------
'''
# 6. Write a program that reads a CSV file a and finds the total sales amount for a specific department
import os
import pandas as pd

dir_path = 'sample'
file_name = 'sales_info.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
total_sales = round(df[df['Department'] == 'Electronics']['Sale_Value'].sum(), 2)
print(f"The total sales amount for Electronics department is: {total_sales}")
'''
# -------------------------------------------------------------------
'''
# 7. Write a program that reads a CSV file and finds the employee with the highest salary
import os
import pandas as pd

dir_path = 'sample'
file_name = 'employees_info.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
max_salary = df['Salary'].max()
max_salary_employee = df[df['Salary'] == max_salary]['Name'].values[0]
print(f"The employee with the highest salary is: {max_salary_employee}")
'''

# -------------------------------------------------------------------
'''
# 8. Write a program that reads a CSV file and generates a bar chart that reperesents the data using Matplotlib
import os
import pandas as pd
import matplotlib.pyplot as plt

dir_path = 'sample'
file_name = 'employees_info.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
plt.figure(figsize=(10,6))
plt.bar(df['ID'], df['Salary'])
plt.xlabel('ID')
plt.ylabel('Salary')
plt.title('Employee Salaries')
plt.show()
'''
# -------------------------------------------------------------------

'''
# 9. Write a function that reads a JSON file and extracts especific information from it.
import os
import pandas as pd
import json

dir_path = 'sample'
file_name = 'countries_info.json'
abs_path = os.path.join(dir_path, file_name)

with open(abs_path, 'r') as f:
    data = json.load(f)
    print(data[0]['Year'])
    print(data[0]['Continent'])
    print(data[0]['Population'])
    print(data[0]['GDP'])
'''
# -------------------------------------------------------------------
'''
# 10. Given a CSV file with temperature data for each day of the week, find the average temperature for each day.
import os
import pandas as pd

dir_path = 'sample'
file_name = 'cities_temperature.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
average_temp = round(df['Temperature'].mean(), 2)
print(f"The average temperature for each day is: {average_temp}")
'''
# -------------------------------------------------------------------
'''
# 11. Write a program that reads a text file and prints its content.
import os

dir_path = 'sample'
file_name = 'file2.txt'
abs_path = os.path.join(dir_path, file_name)

with open(abs_path, 'r') as f:
    content = f.read()
    print(content)
'''
# -------------------------------------------------------------------
'''
# 12. Create a new text file and write some content into it.
import os

dir_path = 'sample'
file_name = 'new_file.txt'
abs_path = os.path.join(dir_path, file_name)

with open(abs_path, 'w') as f:
    f.write("Hello, world!")
    print("Content written to file successfully.")
'''
# -------------------------------------------------------------------
'''
# 13. Implement a program that reads a CSV file and generates a scatter plot that reperesents the data using Matplotlib
import os
import pandas as pd
import matplotlib.pyplot as plt

dir_path = 'sample'
file_name = 'cities_temperature.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
plt.figure(figsize=(10,6))
plt.scatter(df['City'], df['Temperature'])
plt.xlabel('City')
plt.ylabel('Temperature')
plt.title('Temperature vs City')
plt.show()
'''
# -------------------------------------------------------------------