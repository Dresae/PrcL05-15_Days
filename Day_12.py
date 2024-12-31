""" Day 12 Introduction to Pandas for data manipulation and analysis
==========================

1. Given a CSV file with student details, read it into a Pandas dataframe and find the average age of the students.
2. Implement a program that generates a Pandas series with dates and filter it to get dates in a specific range.
3. Write a Python program that uses Pandas to read a CSV file and find maximun and minimum values in a specific column.
4. Create a function that takes a Pandas dataframe and returns a new dataframe with rows sorted in ascending order.
5. Given a Pandas dataframe, filter the rows to include only the rows where a speficic column meets a condition
6. Implement  a program that reads a CSV file into a Pandas dataframe and finds the sum of a specific column
7. Write a function that takes a Pandas dataframe and adds a new calculated column to the dataframe
8. Given a Pandas dataframe, group the data by a specific column and calculate the mean of another column
9. Create a program that reads a JSON file to a Pandas dataframe and extracts specific information from it
10. Implement a function that takes a Pandas dataframe and returns the transpose of the dataframe
11. Create a Pandas series from a list and perform basic operations like filtering, sorting,etc
12. Read a CSV file into a Pandas dataframe and perform basic data manipulation operations
13. Create a Pandas dataframe from a dictionary and perform filtering and grouping operations

"""

# -------------------------------------------------------------------
"""
# 1. Given a CSV file with student details, read it into a Pandas dataframe and find the average age of the students.

import os
import pandas as pd

dir_path = 'sample'
file_name = 'employees_info.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
average_age = round(df['Age'].mean(), 2)
print(f"The average age of the students is: {average_age}")
"""
# -------------------------------------------------------------------
"""
# 2. Implement a program that generates a Pandas series with dates and filter it to get dates in a specific range.

import pandas as pd
import datetime as dt

start_date = dt.datetime(2023, 1, 1)
end_date = dt.datetime(2023, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date)
date_series = pd.Series(date_range)
filtered_dates = date_series[(date_series >= '2023-04-01') & (date_series <= '2023-04-30')]
print(filtered_dates)
"""

# -------------------------------------------------------------------
"""
# 3. Write a Python program that uses Pandas to read a CSV file and find maximun and minimum values in a specific column.

import os
import pandas as pd

dir_path = 'sample'
file_name = 'employees_info.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)

max_value = df['Salary'].max()
min_value = df['Salary'].min()

print(df, '\n')
print(f"Maximum value in the 'Salary' column is: {max_value}")  
print(f"Minimum value in the 'Salary' column is: {min_value}")
"""

# -------------------------------------------------------------------

# 4. Create a function that takes a Pandas dataframe and returns a new dataframe with rows sorted in ascending order.

import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]})

def sort_dataframe(df):
    sorted_df = df.sort_values(by='Age', ascending=True)
    return sorted_df

sorted_df = sort_dataframe(df)

print(sorted_df)