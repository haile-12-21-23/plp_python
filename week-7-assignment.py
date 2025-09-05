# Data Analysis and Visualization
# Author: Hailemariam Terefe


# ---------------------------------
# Task 1: Load and explore dataset
# -----------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris datasets

try:
    iris=load_iris(as_frame=True)
    df=iris.frame
    print('✅Dataset Loaded Successfully')


except FileNotFoundError :
    print("❌ File not found. Please check the dataset path.")
    df=pd.DataFrame() #empty fallback

# Inspect datasets
print('First 5 rows of dataset:')
print(df.head(),'\n')

print('Dataset info:')
print(df.info(), '\n')

print("Missing values per column:")
print(df.isnull().sum())

# clean missing valuees (if any)

df=df.dropna()


# ------------------------------------
# Task 2: Basic Data Analysis
# ------------------------------------
print("Basic Statistics:")
print(df.describe(),'\n')

# Grouping example:mean petal length per species
grouped=df.groupby('target')['petal length (cm)'].mean()
print("Mean Petal Length per Species:")
print(grouped,'\n')

# Pattern/ Finding examples
print("Oveservation: Iris-virginica has the longest average petal length compared to other species.\n ")


# ----------------------------
# Task 3: Data visualization
# ----------------------------

# 1 Line chart (trend  over index, mimicking time series for demo)

plt.figure(figsize=(8,5))
df['sepal length (cm)'].plot(kind='line')
plt.title('Sepal Length Trend')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.grid()
plt.show()

# 2. Bar chart(average petal Length per species)

plt.figure(figsize=(8,5))
sns.barplot(x='target', y='petal length (cm)', data=df, ci=None, palette='viridis')
plt.title('Average Petal Length per Species')
plt.xlabel('Species (0=setosa, 1=versicolor, 2=virginica)')
plt.ylabel('Petal Length (cm)')
plt.show()


# 3. Histogram (distribution of sepal length)

plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of sepal width')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Frequency')
plt.show()


# 4. Scatter plot (relationship between sepal length and petal length)

plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal length (cm)',y='petal length (cm)', hue='target', data=df,palette='deep')
plt.title('Sepal Length Vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
