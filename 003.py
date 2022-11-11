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
    # every increase can be observed
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
    if c==6:
        break;
    # "6" cannot be observed
    print(c)
    c+=1
    
print("\n")

clo = 0
while(clo<10):
    print(clo)
    if clo==6:
        break;
    # "6" will be observed
    clo+=1

# Example

# Create a list of numbers

# Sort the numbers in the list from largest to smallest using a loop

# Print the smallest number of the list

# Print the largest number of the list ?

list3 = [100,300,-89,85,76,-45,34,87,12,0,123]
length2 = len(list3)
temp = 0
for each in range(0,length2):
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
Returns an array with evenly spaced elements as per the interval. 

Syntax : numpy.arange(start,stop,step)

default statement is given arange(stop) 

stop is optional
start is optional
step is required 

("stop" is not involved of array)

Array of evenly spaced values.
Length of array being generated  = ((Stop - Start) / Step) 
 
"""


a1 = np.arange(10) 
print(a1)
a2 = np.arange(1,10)
print(a2)
a3 = np.arange(1,10,2)
print(a3)
 
print("A\n", np.arange(4).reshape(2, 2), "\n") #  [[0 1] [2 3]] 
print("B\n", np.arange(4, 10), "\n")           #  [4 5 6 7 8 9] 
print("C\n", np.arange(4, 20, 3), "\n")        #  [ 4  7 10 13 16 19]

a4 = (np.arange(12).reshape(4, 3)) 
print(a4) #  [[ 0  1  2] [ 3  4  5] [ 6  7  8] [ 9 10 11]]  

print("D\n", np.arange(12).reshape(4, 3),"\n") #  [[ 0  1  2] [ 3  4  5] [ 6  7  8] [ 9 10 11]]  

#linspace
"""
The numpy.linspace() function returns number spaces evenly w.r.t interval. 
Similar to numpy.arange() function but instead of step it uses sample number.

Syntax : 
numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None)

start is required
stop is required 

Others are optional

 
"""
 
a5 = np.linspace(3, 15) 
print(a5)
# The interval between "start" and "stop" was automatically divided by 50.
# Because, default num value is 50.

a6 = np.linspace(3,15,4)
print(a6)
# The interval between "start" and "stop" was divided by 4.

print("\n")

##########################################################################

m1 = np.array([1,2,3])
m2 = np.array([4,5,6])

print("m1+m2 : ",m1+m2)           # m1+m2 :  [5 7 9]
print("m1-m2 : ",m1-m2)           # m1-m2 :  [-3 -3 -3]
print("m1*m2 : ",m1*m2)           # m1*m2 :  [ 4 10 18]
print("m1-m2 : ",m1/m2)           # m1-m2 :  [0.25 0.4  0.5 ]
print("(m1-m2)**2 : ",(m1-m2)**2) # (m1-m2)**2 :  [9 9 9] 


"""
The operations of addition, subtraction, multiplication, and division can be 
calculated since the shapes (dimensions) of m1 and m2 are equal
without using any extra library or function.
"""

"""
m3 = np.array([4,5,6,6,3])
print(m2+m3) # ValueError: operands could not be broadcast together with shapes (3,)  (5,)
"""

# Multiplication of Two Matrices
# Scaler Multiplication
m4 = np.array([[1,2,3,4],[5,6,7,8]])
print(9*m4)

"""

Multiplication in matrices is done between each row
 of the first matrix and each column of the second matrix.

To multiply two matrices, we use dot() method.

"""

h1 = np.array([[3, 6, 7], [5, -3, 0]])   # shape of h1 is 2x3
h2 = np.array([[1, 1], [2, 1], [3, -3]]) # shape of h2 is 3x2
h3 = h1.dot(h2)                          # The row number of h1 is equal to the column number of h2. This condition is required, in order to multiply
print(h3)                                # shape of h3 is 2x2

h4 = np.array([[4,7,2],[1,5,9],[8,3,7],[6,7,1]]) # shape of h4 is 4x3
h5 = np.array([[8,3,7],[6,7,1],[2,7,1],[4,8,4]]) # shape of h5 is 4x3
"""
h4 and h5 cannot be multiplyed because, the row number of h4 is not equal to the column number of h5.
h6 = h4.dot(h5)
print(h6) # ValueError: shapes (4,3) and (4,3) not aligned: 3 (dim 1) != 4 (dim 0)
"""
# To multiply them we need transpose

h6 = h5.transpose()     # shape of h6 is 3x4. h6 is transpose of the h5 whose shape is 4x3.
print(h6)               # [[8 6 2 4] [3 7 7 8] [7 1 1 4]]

h7 = h4.dot(h6)         # shape of h7 is 4x4.    
print(h7)               # [[ 67  75  59  80] [ 86  50  46  80] [122  76  44  84] [ 76  86  62  84]]

# exp()
"""
exp(2) means that e^2. 
"e" is a mathematical constant. 
The value of "e" is about 2.71828
exp(2) = e^2 = (2.71828)^2

"""

h8 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) 
print(h8)
h9 = np.exp(h8)
print(h9)


print("\n")


#####################################################################

# ** operator
"""
The double asterisk, ** operator is a shortcut to calculate the exponential value. 
Let’s take a look at how this can be used in the following code:
"""
base = 3
exponent = 4
print ("Exponential Value is: ", base ** exponent)

# pow( ) 
"""
In addition to the ** operator, Python has included a built-in pow() function 
which allows users to calculate the exponential value.

The function takes as input the base and exponent and returns the corresponding value. 
The general syntax of the function is:
"""
base2 = 5
exponent2 = 3
ex1 = pow(base2, exponent2)
print(ex1)

# exp()
"""
The exp() function in Python allows users to calculate 
the exponential value with the base set to e.

Note :
    e is a Mathematical constant, with a value approximately equal to 2.71828.
    The math library must be imported for this function to be executed.
"""
exponent3 = 4
print ("Exponential Value is: ", np.exp(exponent3))


#######################################################################

# random()
"""
Returns a random float number between 0 and 1.
There are many "random" types.
Click for more" https://www.w3schools.com/python/module_random.asp "
"""
r1 = np.random.random((3,5))
print("Randomly generated matrix r1 :\n",r1) 

print("Minimum of r1 :",r1.min())
print("Maximum of r1 :",r1.max())

print("Sum of r1 :", r1.sum())

print("Sum of columns of r1 :",r1.sum(axis=0))

print("Sum of rows of r1 :",r1.sum(axis=1))

#######################################################################

# sqrt()
# square()

r2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(r2) # [[1 2 3][4 5 6][7 8 9]]

r3 = np.square(r2)
print(r3) # [[ 1  4  9][16 25 36][49 64 81]]

r4 = np.sqrt(r3)
print(r4) # [[1. 2. 3.][4. 5. 6.][7. 8. 9.]]

#######################################################################

r5 = np.array([0,1,2,3,4,5,6,7,8,9])
print(r5[0])    # index 0 will be printed
print(r5[:5])   # indexes will be printed from index 0 to index 5 ( index 5 is not included )
print(r5[::-1]) # all indexes will be printed as a reversa

r6 = np.array([[1,2,3,4],[5,6,7,8]])
print(r6)          # [[1 2 3 4][5 6 7 8]]
print(r6[::-1])    # [[5 6 7 8][1 2 3 4]]

print(r6[:-1])     # [[1 2 3 4]]
print(r6[-1:])     # [[5 6 7 8]]

print(r6[0:2,1:3]) # [[2 3][6 7]]
print(r6[0:2,2:4]) # [[3 4][7 8]]

print(r6[0,1])     # 2
print(r6[0,2])     # 3
print(r6[0,1:3])   # [2 3 ]

print(r6[1,2])     # 7
print(r6[1,3])     # 8
print(r6[1,2:4])   # [7 8]

print(r6[1,0:4])   # [5 6 7 8]
print(r6[1,:4])    # [5 6 7 8]
 
print("\n")
#######################################################################

# ravel() - could be question for the lab exam
"""
np.ravel() functions returns contiguous flattened array.
 A copy is made only if needed. 
"""
r7 = np.array([[12,24,36,48],[60,72,84,96],[108,120,132,144]])
print(r7)           # [[ 12  24  36  48][ 60  72  84  96][108 120 132 144]]
print("\n")

r8 = r7.ravel();
print(r8)           # [ 12  24  36  48  60  72  84  96 108 120 132 144]
print("\n")

r9 = r8.reshape(2,6)
print(r9)           # [[ 12  24  36  48  60  72][ 84  96 108 120 132 144]]        
print("\n")

r10 = r9.T
print(r10)          # [[ 12  84][ 24  96][ 36 108][ 48 120][ 60 132][ 72 144]]
print("\n")

print("\n")
#######################################################################

# differences between reshape and resize - could be question for the lab exam

r11 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
print(r11)         # [[ 1  2  3  4  5  6][ 7  8  9 10 11 12][13 14 15 16 17 18]]

"""
If you do not assign any variable after using the "reshape()" function, 
your action will not be permanent. 
Because "reshape()" does not change the "array" on which it operates.
"""
print(r11.reshape(9,2))     # [[ 1  2][ 3  4][ 5  6][ 7  8][ 9 10][11 12][13 14][15 16][17 18]]
"""
The action was executed but not saved anywhere.
"""
r12 = r11.reshape(9,2)      # The action was saved to r12.
print(r12)                  # [[ 1  2][ 3  4][ 5  6][ 7  8][ 9 10][11 12][13 14][15 16][17 18]]
print("\n")            

print(r11)                  # [[ 1  2  3  4  5  6][ 7  8  9 10 11 12][13 14 15 16 17 18]]
print("\n")                 # r11 is still same

"""
After using "resize()", the variable being operated on changes.
No need to save anywhere after using resize()
"""

r11.resize(1,18)            # The size of r11 was changed
print(r11)                  # [[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18]]
print("\n")
