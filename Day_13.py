""" Day 13 Data Visualization with Matplotlib and Seaborn
==========================

1. Given a Pandas Dataframe, create a line plot to visualize the trend of a specific column over time.
2. Implement a program that generates a histogram using Matplotlib to visualize the distribution of data.
3. Write a Python program that uses Seaborn to create a scatter plot matrix for multiple variables in a dataframe.
4. Create a function that takes a Pandas dataframe and generates a box plot to visualize the distribution of data.
5. Given a CSV file with sales data, uses Matplotlib to create a bar plot to compare the sales of different products.
6. Implement a program that reads a JSON file into a Pandas dataframe and uses seaborn to create a violin plot.
7. Write a function that takes a Pandas dataframe and generates a pair plot to visualize the relationship between variables.
8. Given a Pandas dataframe, creae a pie chart using Matplotlib to visualize the distribution of data.
9. Create a program that reads a CSV file into a Pandas dataframe and uses Seaborn to create a swarm plot.
10. Implement a function that takes a Pandas dataframe a generates a heatmap using Seaborn to visualize the correlation between variables.
11. Create a simple line plot using Matplotlib to visualize a series of data points.
12. generate a scater plot using Matplotlib to visualize the relationship between two variables.
13. Generate a bar plot using Seaborn to compare the categories in a dataset.

"""

# -------------------------------------------------------------------

# 1. Given a Pandas Dataframe, create a line plot to visualize the trend of a specific column over time.

import os
import pandas as pd
import matplotlib.pyplot as plt

dir_path = 'sample'
file_name = 'autopart_sales.csv'
abs_path = os.path.join(dir_path, file_name)

df = pd.read_csv(abs_path)
df = df[['Product_Name', 'Units_Sold', 'Sales_Person', 'Sale_Date','Sales_Profit']]

df['Sale_Date'] = pd.to_datetime(df['Sale_Date']) # set the column as datetime data type
df['Month'] = df['Sale_Date'].dt.strftime('%b') # convert to month name 

df.plot(x='Month',y='Units_Sold', kind='line')
plt.title('Sales Trend For FY-2024')
plt.xlabel('FY-2024')
plt.ylabel('Units Sold')
plt.show()

#print(df)

# -------------------------------------------------------------------