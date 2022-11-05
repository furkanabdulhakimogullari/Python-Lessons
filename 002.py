# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:33:04 2022

@author: furkan
"""
#function parameter

def my_first_function(a,b):
    """
    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    
    """
    temporary_value = a
    a = b
    b = temporary_value
    output = ( a + b ) / ( a - b )
    
    return output

my_first_function(45, 56)
print("My first function is",my_first_function(1, 2))

def circumference_of_circle(r,pi=3.14):
    circumference = 2*pi*r
    return circumference

circumference_of_circle(5)
print("The circumference of the circle is",circumference_of_circle(5)," cm")

#list

list1 = [1,2,3,4,5,6] # list can be made with integers
list2 = ["ali", "veli", "deli"] # list can be made with strings
type(list1)
# type() statement gives type of variable

index0 = list1[0] # first index
index1 = list1[1] # second index
index2 = list1[2] # third index
index3 = list1[3] # fourth index
index4 = list1[4] # fifth index
index5 = list1[5] # sixth index (last index)

index5_ = list1[-1] # sixth index (last index)
index4_ = list1[-2] # fifth index
index3_ = list1[-3] # fourth index
index2_ = list1[-4] # third index
index1_ = list1[-5] # second index
index0_ = list1[-6] # first index
 
index = list1[0:3] # gives index_0 , index_1 , index_2 ( index_3 is not given )   

dir(list1)
# dir(list1) statement gives functions that list1 can use

list3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list4 = ["ayse", "fatma", "hayriye"]

help(list.append)
# Append object to the end of the list.
# append(self, object, /)
list3.append(50)
list4.append("cifte telliye")

help(list.remove)
# Remove first occurrence of value.
# Raises ValueError if the value is not present.
# remove(self, value, /)
list3.remove(7)
list4.remove("fatma")

help(list.reverse)
# Reverse *IN PLACE*.
# reverse(self, /)
list3.reverse()
list4.reverse()

help(list.sort)
# Sort the list in ascending order and return None.  
# The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).  
# If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.  
# The reverse flag can be set to sort in descending order.
# sort(self, /, *, key=None, reverse=False)
list5 = [45,23,89,35,28,79,93,82]
list6 = ["zonguldak","manisa","ankara","balikesir"]
list7 = ["a",4,"r",9,46,"b","z",1,"c",99]
list5.sort()
list6.sort()
# list7.sort() #TypeError 
# '<' not supported between instances of 'int' and 'str'

help(list.clear)
# Remove all items from list.
# clear(self, /)
list8 = [1,4,67,3,9,57]
list8.clear()

help(list.copy)
# Return a shallow copy of the list.
# copy(self, /)
list9 = [1,4,67,3,9,57,23,45,80,14]
list10 = list9.copy()

help(list.count)
# Return number of occurrences of value.
# count(self, value, /)
list11 = [3,7,1,0,45,8,2,6,423,1,89,32,3,4,3,3]
a = list11.count(2) # a is 1 because there is a just "2" 
b = list11.count(3) # b is 4 because there are 4 "3"

help(list.extend)
# Extend list by appending elements from the iterable.
# extend(self, iterable, /)
list12 = [1,2,3,4,5,67,8,9,922,21,56]
c = [99,88,77,66,55,44,33,22,11]
list12.extend(c)

help(list.index)
# Return first index of value.
# Raises ValueError if the value is not present.
# index(self, value, start=0, stop=9223372036854775807, /)
list13 = ["c++","python","java","c","react"]
d = list13.index("c")


help(list.insert)
# Insert object before index.
# insert(self, index, object, /)
list14 = ['a','g','k','b','p','t']
list14.insert(5, 'z')

help(list.pop)
# Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
# pop(self, index=-1, /)
list15 = [2, 3, 5, 7]
e = list15.pop(3)

#tuple
"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.
"""
tuple1 = (1,2,3,4,5,6,7)
dir(tuple1)
type(tuple1)

help(tuple.count)
# Return number of occurrences of value.
# count(self, value, /)
tuple2 = ('a','b','c','d','e','a')
f = tuple2.count('a')

help(tuple.index)
# Return first index of value.
# Raises ValueError if the value is not present.
tuple3 = ('a','k','o','y','r','q','m')
g = tuple3.index('y')

#Dictionary
"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

dict1 = {"name":"furkan", "surname":"AHO","age":23,"school":"IUC", 17:"favourite number"}
h = dict1["name"]
j = dict1["age"]
k = dict1[17]

keys1 = dict1.keys()
values1 = dict1.values()

#conditions if-elif-else

var100 = 10
var99 = 34

if(var100>var99):
    print("10>34")
elif(var100<var99):
    print("10<34")
else:
    print("10=34")
    

numbers = [1,2,3,4,5,6,7,8,9,10]

if 44 in numbers:
    print("false")
elif 4 in numbers:
    print("true")
else:
    print("false")
    
#example_1

def yeartocentury(year):
    if(year < 100):
        return 1
    elif(year/100 > 1):
        return int(year/100 + 1)
    
        
print(yeartocentury(1999))

'Rishu'[0::-1].replace('R','r')
