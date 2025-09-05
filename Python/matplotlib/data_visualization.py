# Data Visualization with matplotlib

# Introduction to matplotlib

# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in python.
# It is often used for visualizing the results of data analysis.
# The most common form of visualization is through line plots, scatter plots, bar plots, and histograms

# Basic Plotting with matplotlib


# Simple line Plot:

import matplotlib.pyplot as plt
import pandas as pd

# Plotting Age vs Name


data={'Name':['Alice','Bob','Charlie'],
      'Age':[25,30,35],
      'City':['New York','Los Angeles','Chicago']}

plt.plot(data['Name'],data['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name Vs Age')
plt.show()

# Bar Plot

# Plotting bar chart for Age by city

df=pd.DataFrame(data)
df.groupby('City')['Age'].mean().plot(kind='bar')

plt.xlabel('City')
plt.ylabel('Average of Age')
plt.title('Average Age by City')
plt.show()


# HistoGram plot

# Plotting a histogram for Age

df['Age'].plot(kind='hist',bins=10)
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()


# Scatter Plot:

# Plotting a scatter plot of Age vs City
df.plot(kind='scatter',x='City', y='Age')
plt.title('City Vs Age')

plt.show()


# Customizing plots

# Adding Labels and Title:
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')

#Color and Style
df['Age'].plot(kind='line',color='green',linestyle='--', linewidth=2)
