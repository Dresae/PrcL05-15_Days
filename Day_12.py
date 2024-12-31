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
"""
# 4. Create a function that takes a Pandas dataframe and returns a new dataframe with rows sorted in ascending order.

import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]})

def sort_dataframe(df):
    sorted_df = df.sort_values(by='Age', ascending=True)
    return sorted_df

sorted_df = sort_dataframe(df)

print(sorted_df)
"""
# -------------------------------------------------------------------
"""
# 5. Given a Pandas dataframe, filter the rows to include only the rows where a speficic column meets a condition

import pandas as pd 

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]})
filtered_df = df[df['Age'] >= 30]

print(filtered_df) 
"""
# -------------------------------------------------------------------
"""
# 6. Implement  a program that reads a CSV file into a Pandas dataframe and finds the sum of a specific column

import os
import pandas as pd

dir_path = 'sample'
file_name = 'products.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
Quantity_sum = df['Quantity'].sum()

print(f"The total products stock is: {Quantity_sum}")
"""
# -------------------------------------------------------------------
"""
# 7. Write a function that takes a Pandas dataframe and adds a new calculated column to the dataframe

import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]})
df2 = df.copy()

def add_calculated_column(df2):
    df2['Calculated'] = df2['Age'] * 2
    return df2

df_added = add_calculated_column(df2)

print("Initial DataFrame: ", '\n',df,'\n')
print("New DataFrame: ", '\n', df_added)
"""

# -------------------------------------------------------------------
"""
# 8. Given a Pandas dataframe, group the data by a specific column and calculate the mean of another column

import os
import pandas as pd 

dir_path = 'sample'
file_name = 'autoparts_sales.csv'
abs_path = os.path.join(dir_path, file_name)
df = pd.read_csv(abs_path)

# 1. Define calculated columns
df['Sales_Total'] = df['Units_Sold'] * df['Unit_Price']
df['Sales_AVG'] = df['Sales_Total'] / df['Units_Sold']
df['Profit_Margin_AVG(%)'] = ((df['Sales_Profit'] / df['Sales_Total']) * 100)

# 2. Group the data by Product and calculate the mean of Quantity, Cost and Profit
KPI_Table = df.groupby('Sales_Person').agg({'Units_Sold': 'sum', 'Sales_Total': 'sum', 'Sales_AVG': 'mean',  'Sales_Profit': 'sum', 'Profit_Margin_AVG(%)': 'mean'})

print("Sales Report: ", '\n', KPI_Table)
"""

# -------------------------------------------------------------------
"""
# 9. Create a program that reads a JSON file to a Pandas dataframe and extracts specific information from it

import os
import pandas as pd 

dir_path = 'sample'
file_name = 'countries_info.json'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_json(abs_path)
extracted_data = df.sort_values(by='GDP', ascending=False)[['Country', 'GDP']]

print("Countries GDP: ", "\n", extracted_data)
"""
# -------------------------------------------------------------------
"""
# 10. Implement a function that takes a Pandas dataframe and returns the transpose of the dataframe

import pandas as pd

data = {
    'Computer': [2500, 3400, 3400, 680],
    'Laptop': [1500, 1750, 2000, 2500],
    'Tablet': [800, 900, 1000, 1200],
    'Smartphone': [500, 600, 700, 800]
}
months = ['January', 'February', 'March', 'April']
df = pd.DataFrame(data, index=months)


def transpose_dataframe(df):
    return df.T
df_transposed = transpose_dataframe(df)

print("Original DataFrame: ", '\n', df, '\n')
print("Transpose DataFrame: ", '\n', df_transposed)
"""
# -------------------------------------------------------------------
"""
# 11. Create a Pandas series from a list and perform basic operations like filtering, sorting,etc

import pandas as pd

my_list = [0.548, 0.35, 0.025, 0.1052, 0.0548, 0.24, 0.8025, 0.0245, 0.152, 0.245]
series = pd.Series(my_list)

print("ORIGINAL SERIES: ", '\n', series, '\n')

filtered = series[series > 0.14].sort_values()
print("FILTERED SERIES: ", '\n', filtered, '\n') # Series with values greater than 0.14

sorted = series.sort_values(ascending=False)
print("SORTED SERIES: ", '\n', sorted, '\n')    # Series sorted in descending order
"""

