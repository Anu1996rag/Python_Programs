# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 08:59:35 2019

@author: Gurudas

Arrays in Python

"""

#program to create an integer type array

#array module in python to create arrays of similar datatype

import array
#creating array
a = array.array('i',[2,3,4,5]) # i stands for integer typecode

#printing elements
for element in a:
    print(element,end=" ")

#program to create array of unicode characters
    
a = array.array('u',['q','q','w','g']) #u stands for unicode character not strings 

for i in a:
    print(i,end=" ")

#creating an array based on another array

#taking array a from the previous program 

a2 = array.array(a.typecode,(i+2 for i in a))
print(a2)

########################## INDEXING AND SLICING #########################################

from array import *

arr1 = array('i',[1,3,4,5,6,6])

n = len(arr1) #length of the array arr1

#displaying elements using indexing
for i in range(n):
    print(arr1[i],end =" ")
    
#program to retrieve elements using while loop


arr1 = array('i',[1,3,4,5,6,6])

n = len(arr1) #length of the array arr1

i = 0

while i<n:
    print(arr1[i],end=' ')
    i+=1
    
#program to show the effects of slicing operations of the array
    
x = array('i',[1,3,4,5,6,6])

#create an array y with elements from 1st to 3rd from x

y = x[1:4]
print(y)

#create an array y with elements from 0th till last element in x

y = x[0:]
print(y)

#create an array y with elements from 0th to 3rd from x

y = x[:4]
print(y)

#create an array y with last 4 elements from x

y = x[-4:]
print(y)

#create an array y with last 4th element and with 3 elements towards right

y = x[-4:-1]
print(y)

#create an array y with elements from 0th till last element in x
#stride 2 means after 0th element , retrieves 2nd element from x

y = x[::2]
print(y)

######################## PROCESSING ARRAYS #####################################

x = array('i',[1,3,4,5,6,6])

#appending 30 to the array

x.append(30)
print(x)

#insert 99 in the array in the position 1

x.insert(1,99)
print(x)

#remove an element from array

x.remove(6) #removes the first occurrence of the element in an array
print(x)

#remove the last element of the array using the pop() method

print(x.pop())

#finding the position of an element using the index() method

print(x.index(5))

#converting an array into list using tolist() method

y = x.tolist()

#displaying the types of the arrays

print(type(x))
print(type(y))


#program to store a student's marks and displaying the total marks and the percentage

string = input("Enter students marks :").split()

marks = [int(i) for i in string]

n = len(marks)

sum_marks = 0

for x in marks:
    print(x)
    sum_marks += x
    
total_marks = sum_marks

percent = total_marks / n

print("Total Marks :",total_marks)
print("Percentage :",percent)


######################### SORTING USING BUBBLE SORT #############################
#sorting the elements in the given array using bubble sort technique

n = int(input("Enter no. of element you want to insert :"))

x =array('i',[]) #empty array

for i in range(n): #repeat for n times
    print("Enter element :",end="") 
    x.append(int(input()))#add element to the array x

print("Original Array : ",x)

#### bubble sort ########

flag = False #when swapping is done , flag becomes true

for i in range(n-1): #i from 0 to n-1
    for j in range(n-1-i): #j from the first element to one less than that of i
        if x[j] > x[j+1]: #if the first element is greater than the second
            x[j],x[j+1] = x[j+1],x[j] #swapping the elements
            flag = True #swapping is done here
    
    if flag == False:
        break #means swapping is not performed i.e. array is in sorted order and comes out of inner for loop
    else:
        flag = False #assign initial values to the flag

print("Sorted Array :",x)
            

########################### LINEAR/SEQUENTIAL SEARCH #############################

n = int(input("Enter no. of elements :"))

x = array('i',[])

for i in range(n):
    print("Enter element :",end="")
    x.append(int(input()))

print("Original Array :",x)

s = int(input("Enter element you want to search:"))

flag = False

for i in range(len(x)):
    if s == x[i]:
        print("Element found at position :",i+1)
        flag = True
    
if flag == False:
    print("Element not found")
        

#program to search for an element in an array using the index() method
    
n = int(input("Enter no of elements :"))

x = array('i',[]) #empty array

for i in range(n):
    print("Enter element :",end="")
    x.append(int(input()))

print("original array :",x)

s = int(input("Enter element to search :"))

try:
    pos = x.index(s)
    print("Element found at position",pos+1)
except ValueError:
    print("Element not found")
    

####################### COMPARING ARRAYS ##########################################

#program to compare each element in the array and retrieve the largest one using where() method

import numpy as np

a = np.array([10 ,20,30,40,50],dtype=int)
b = np.array([45,20,62,3,40],dtype=int)            

c = np.where(a>b,a,b)

print(c)
    

#################### ALIASING ARRAYS ################################################


a = np.array([10 ,20,30,40,50],dtype=int)
b = a #aliasing array a to b

print("Original arrays :",a,b,end="\t")

b[0]=99 #dding an element in the array b

print("After modification : ",a,b)


################### VIEWING AND COPYING ARRAYS ##################################

a = np.array([10 ,20,30,40,50],dtype=int)
b = a.view() #view method to copy the elements from a 

print("Original Array :",a)
print("New array :",b)

b[0]=21

print("Afer Modification :")

print("Original Array :",a)
print("New array :",b)


#program 2


a = np.array([10 ,20,30,40,50],dtype=int)
b = a.copy() #view method to copy the elements from a 

print("Original Array :",a)
print("New array :",b)

b[0]=30

print("Afer Modification :")

print("Original Array :",a)
print("New array :",b)

#program to retrieve elements from a 3d array

a = [[[1,2,3],[4,5,6]],
     [[7,8,9],[10,11,12]]]

#displaying element by element

for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k],end="\t")
        print()
    
    