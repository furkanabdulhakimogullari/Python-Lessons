# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:29:25 2022

@author: furkan
"""
#pandas
"""
Pandas is an abbreviation for Python Data Analysis Library. 

It is an open-source library specially designed for data analysis 
and data manipulation in Python.

Pandas is built on the top of the NumPy package and hence it 
fundamentally relies on NumPy.

Pandas enable us to read from multiple sources such as Excel, 
CSV, SQL, and many more.

Basically, Pandas possess two types of data objects:   
Pandas DataFrame: 
    It is a mutable two-dimensional data structure with 
    labeled rows and columns which are generally compared with excel 
    and SQL sheets.
Pandas Series: 
    It is a One-dimensional labeled array to store the heterogeneous 
    data elements generally compared with the columns in MS Excel.
    
Click for more : https://favtutor.com/blogs/numpy-vs-pandas
"""

import pandas as pd

dict1 = {
    "Name":["furkan","faruk","muhammed","nermin","sedat"], 
    "Age" :[24,18,15,45,50],
    "Experience":[4,3,2,6,5]
    }

dataFrame1 = pd.DataFrame(dict1)

head1 = dataFrame1.head()
tail0 = dataFrame1.tail(3)
tail1 = dataFrame1.tail(2)
tail2 = dataFrame1.tail(1)
tail3 = dataFrame1.tail(0)

print(dataFrame1)
print(dataFrame1.columns) 
# Carefull!! In this situation, dtype is normally string.
# But, now dtype is object because of using "pandas" library.

print("\n")
####################################################################

# In order to get information about DataFrame, .info() extension is used.
print(dataFrame1.info())

print("\n")
####################################################################

"""
The describe() method is used for calculating some statistical data like 
percentile, mean and std of the numerical values of the Series or DataFrame. 
It analyzes both numeric and object series and also the DataFrame 
column sets of mixed data types.
"""

print(dataFrame1.describe())

print("\n")
####################################################################

# Indexing
print(dataFrame1.Age)
print(dataFrame1["Age"])

print("\n")
####################################################################

# Adding new column into dataFrame1
dataFrame1["Salary"] = [50,300,1000,2000,1500]
dataFrame1["Gender"] = ["male","male","male","female","male"]

print(dataFrame1.loc[:,"Age"])
# All indexes of "Age" column.

print(dataFrame1.loc[0:2,"Age"])
print(dataFrame1.loc[:2,"Age"])
# All objects of "Age" index 0 to index 2

print(dataFrame1.loc[1:3,"Age":"Salary"])
# All objects from index 1 to index 3 ( 3 is included ) between "Age" and "Salary"

print(dataFrame1.loc[::-1,:])
# All objects are in reverse order

print("\n")
####################################################################

mean_of_salary = dataFrame1.Salary.mean()
print(mean_of_salary)

dataFrame1["Salary status"] = ["low" if mean_of_salary > each else "high" for each in dataFrame1.Salary]
















