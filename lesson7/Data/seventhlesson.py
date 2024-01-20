# Import pandas

import pandas as pd


import os

file_path = 'Salaries.csv'
if os.path.exists(file_path):
    print("Hello")
else:
    print(f"The file {file_path} does not exist.")


# Read this csv into a dataframe called df


df = pd.read_csv('Salaries.csv', header=0, encoding='utf-8')
print(df)

# What are the columns names?

df.columns

# What are data types of columns we have in this data frame?

df.dtypes

# Select rank, gender and salary columns and display the results on screen

df_salary = df[['rank','gender','salary']]
print(df_salary)

# Write the selected columns from the previous task to a new csv file called selected_salaries.csv

df_salary.to_csv("Data\selected_salaries.csv")