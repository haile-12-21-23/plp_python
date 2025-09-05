# What is Pandas?
# Pandas is an open-source python library that provides high-performance, easy-to-use data structures and data structure and analysis tools.
# It is primarily used for working with tabular data in the form of DataFrames.
# It allows to efficiently manipulate, clean and analyze structured data.

# Series: A one-dimensional labeled array that can hold any data type (integers, strings, etc.)
# DataFrame:A two-dimentional, size-mutable, potentially hetrogeneous tabular data structure with labeled axes(row and column).

# Key Operation in Pandas:

# Creating DataFrames:Create Dataframe by loading data from various formats like CSV,Excel, or SQL databasee,

# For Example
import pandas as pd

#Creating DataFrame from a dictionary.

data={'Name':['Alice','Bob','Charlie'],
      'Age':[25,30,35],
      'City':['New York','Los Angeles','Chicago']}
df=pd.DataFrame(data)

print("Created DataFrame:",df)

# Reading Data: pandas allows you to load data from multiple sources,such as CSV,Excel, or SQL databases.

# Reading data from a CSV file
df=pd.read_csv("data.csv")
print("DataFrame from CSV:",df)

# Manipulating DataFrames:
# 1 Selecting Columns:Can select a specific column.
df['Age'] #Selects the Age of Column
# 2 Filtering Rows:Filter rows based on a condition

df[df['Age']>30] #Return rows where age is greater than 30

# Adding/Removing Columns:

df['Country']=['USA', 'USA', 'USA'] #Adding new column

df.drop('Country',axis=1, inplace=True) #Drop the Country column

# Multiple conditions:combine multiple conditions using logical operators:

# Get rows where Age is greater than 30 and City is "New York"
df_filtered=df[(df['Age']>30)& (df['City']=='New York')]



#Sorting Data:
# Sorting by columns:Sort the dataframe by column in ascending or descending order.

df_sorted=df.sort_values(by='Age',ascending=False) #Sort by age in descending order.

# Sorting by multiple columns

df_sorted=df.sort_values(by=['Age','City'], ascending=[True,False]) #Sort by age in ascending order and city in descending order.

# Aggregating data
# Groupby: pandas groupby method is essential for aggregating data based on one or more columns.

# For Example

grouped=df.groupby('City').agg({'Age':'mean','Name':'count'})

# Summarized Statistics: Pandas provide several builtin funtions to calculate summary statistics.

df['Age'].mean() #Mean of Age columsn
df['Age'].sum() #Sum of Age colums
df['Age'].max() #Max of Age columns
df['Age'].min() #Min of Age columns
