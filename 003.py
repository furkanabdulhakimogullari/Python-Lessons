# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:38:37 2022

@author: furkan
"""
#loops

#for

for each in range(0,10):  
    #from 0 to 10 (10 not included)
    print(each)
   
for each in "kalk appiah kalk allah'ın dedigi olur":
    print(each)

# split()
"""
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.

syntax : string.split(separator, maxsplit)

seperator :
Optional. 
Specifies the separator to use when splitting the string. 
By default any whitespace is a separator.

maxsplit :
Optional. 
Specifies how many splits to do. 
Default value is -1, which is "all occurrences"

"""

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x) # ['apple', 'banana', 'cherry', 'orange']

txt2 = "hello, my name is Peter, I am 26 years old"
x2 = txt2.split(", ")
print(x2) # ['hello', 'my name is Peter', 'I am 26 years old']

txt3 = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 2, will return a list with 3 elements!
x3 = txt3.split("#", 2)
print(x3) # ['apple', 'banana', 'cherry#orange']

for each in "kalk appiah kalk allah'ın dedigi olur".split():
    print(each)

# sum()
"""
The sum() function returns a number, the sum of all items in an iterable.

syntax : sum(iterable, start)

iterable : 
Required. 
The sequence to sum

start :	
Optional. 
A value that is added to the return value
"""

a = (1, 2, 3, 4, 5)
x = sum(a)
print(x) # (1+2+3+4+5) = 15

b = (1, 2, 3, 4, 5)
x2 = sum(b, 7)
print(x2) # 7 + (1+2+3+4+5) = 7 + 15 = 22

list1 = [1,3,5,7,9,11,13,15,17,19,21]

count = 0
for each in list1 :
    count = count + each
    # every increase can be observed
    print(count) 

count2 = 0
for each in list1 :
    count2 = count2 + each
# only last value can be observed
print(count2)    

# while

i=0
while(i<9):
    print(i)
    i = i + 1

# len()
"""
The len() function returns the number of items in an object.
When the object is a string, the len() function returns the number of characters in the string.

syntax : len(object)

object :	
Required. 
An object. 
Must be a sequence or a collection

"""
mylist = "Hello"
x = len(mylist)
print(x) # 5

list2 = [1,3,5,7,9,11,13,15,17,19,21]
length = len(list2)
each = 0
count3 = 0
while (each<length):
    count3 = count3 + list2[each]
    each = each + 1 # each+=1
print(count3)

c = 0
while(c<10):
    print(c)
    if c==6:
        break;
    c+=1
    
print("\n")

# Example

# Create a list of numbers

# Sort the numbers in the list from largest to smallest using a loop

# Print the smallest number of the list

# Print the largest number of the list ?

list3 = [100,300,-89,85,76,-45,34,87,12,0,123]
length2 = len(list3)
temp = 0
smallest = 0
for each in range(0,length2):
    # smallest = list3[each]
    for each2 in range(0,length2):
        if list3[each]>list3[each2]:
            temp = list3[each]
            list3[each] = list3[each2]
            list3[each2] = temp      


for each3 in range(0, length2):
    print(list3[each3]," ")

print("\n")
print("The smallest number of the list is",list3[length2-1])
print("The largest number of the list is",list3[0])

#import

"""
NumPy is a Python library.
NumPy is used for working with arrays.
NumPy is short for "Numerical Python".

"""

#shape
"""
The shape of an array is the number of elements in each dimension.

NumPy arrays have an attribute called shape that returns a tuple 
with each index having the number of corresponding elements.

"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr.shape) # (5,)

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr2.shape)  # (2,4)

arr3 = np.array([1, 2, 3, 4], ndmin=5)
print(arr3)
print('shape of array :', arr3.shape)
print("\n")

#reshape
"""
Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.

"""

arr4 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr4)
print("shape of arr4 :",arr4.shape)
print("\n")

newarr4=arr4.reshape(2,5)
print(newarr4)
print("shape of new arr4 :",newarr4.shape)
print("\n")

# ndim
# gives the dimension of the array

arr5 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr5)
print("The shape of arr5 :",arr5.shape)                 # (10,)
print("The dimension of arr5 :",arr5.ndim)              #  1
print("The data type of arr5 :",arr5.dtype.name)        # int32 
print("The size of arr5 :",arr5.size)                   #  10
print("\n")

newarr5=arr5.reshape(5,2)
print(newarr5)
print("The shape of new arr5 :",newarr5.shape)          # (5, 2)
print("The dimension of arr5 :",newarr5.ndim)           #  2
print("The data type of newarr5 :",newarr5.dtype.name)  # int32
print("The size of arr5 :",arr5.size)                   #  10
print("\n")

#allocation

zeros1 = np.zeros((3,5))    # set all indexs as zero
zeros1[2,4] = 8
zeros1[1,1] = 4
 
ones1 = np.ones((6,7))      # set all indexs as one
ones1[3,5] = 34

empty1 = np.empty((7,11))   # set all indexs as empty
empty1[4,8] = 67

 #arange
"""
 
"""
 


