# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:09:21 2019

@author: Gurudas

Control Statements
"""

#Program to calculate the area of the circle

from math import pi

rad = float(input("Enter radius of a circle:"))

area = pi * rad **2

print("area of a circle = ",area)

print("Area of a circle = {:0.2f}".format(area))



#to check if a given no. is odd or even 

num = int(input("Enter a no."))

if num % 2 ==0:
    print("it is an even no.")
else:
    print("it is an odd no.")
    

#to check whether a no is in between 1 and 10
    
n = int(input("Enter a no :"))

if n <= 10 and n>=1:
    print("No. is in between 1 and 10")
else:
    print("no. is not in between 1 and 10")
    
#to check whether a given no is positive , negative or zero
    
n = int(input("Enter a no:"))

if n > 0:
    print("The no. is positive.")
elif n<0:
    print("The no. is negative.")
else:
    print("The no. is zero.")
    
#to accept no from keyboard and display it in the words
    
n = int(input("Enter a no:"))

if n == 0 : print("Zero")
elif n == 1 : print("One")
elif n == 2 : print("Two")
elif n == 3 : print("Three")
elif n == 4 : print("Four")
elif n == 5 : print("Five")
elif n == 6 : print("Six")
elif n == 7 : print("Seven")
elif n == 8 : print("Eight")
elif n == 9 : print("Nine")
else: print("Please enter a no. between 0-9...")

#to display numbers 1 to 10 using while loop

x = 1
while x <= 10:
    print(x)
    x +=1

#to display even nos between 100 to 200
    
x = 100

while x >=100 and x<=200:
    print(x)
    x +=2

#to display odd nos between two given nos.

m,n = map(int,input("Enter the minimum and maximum range :").split())

x = m  #to start from the first given nos
if x%2==0: #if the given no is even then start with the next nos.
    x +=1

while x <=n:
    print(x)
    x+=2

#to display each characters using for loop
    
str = "Hello World !"

for ch in str:
    print(ch)
    
#to display each character from a string using sequence index

str = "Hello"

n = len(str) #to store the no of characters of a string

for i in range(n):
    print(str[i])
    
#program to display odd nos using for loop
    
for i in range(1,20,2): #2 means the i will iterate with 1 step increment 
    print(i)

#to display nos in descending order using for loop

for i in range(10,0,-1):
    print(i)

#to display elements of a list using for loop
    
a = ['sdf',234,'234d',34]

for i in a:
    print(i)

#to display the sum of the numbers from a list

a = [10,20,30,40,50]

s = 0

for i in a :
    print(i)
    s = s + i
print(s)

#to display numbers from a list and their sum using while loop

l  = [10,20,30,40,50]
n = len(l)  #length of a list

i = 0 #variable initialization

s = 0 

while i<n:
    s = s + l[i] #element of the list
    i += 1 #incrementing the counter
print(s)


#################################### Nested Loops #########################################

for i in range(4):
    for j in range(3):
        print("i=",i,"j=",j,end="\n")
    
#to display a pattern 
        
for i in range(1,11):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#to display an equilateral triangle 

n = 20

for i in range(1,11):
    print(' '*n , end=" ")#repeating space for n times
    print("* "*(i)) #repeating star for i times
    n -=1 

#to display nos from 1 to 100 in a proper format

for i in range(1,11):
    for j in range(1,11):
        print('{:3}'.format(i*j),end=" ")
    print()


##################### THe ELSE Suite ################################################
    
#program to search for an element in the list 
    
a = [10,20,30,40,50]

search = int(input("Enter an element to search :"))

for i in a :
    if search == i:
        print("Element found in the list")
        break
    else:
        print("Element not found in the list")

###################### BREAK Statement##########################################


#program to display nos from 10 to 6 and break the loop when the nos is about to display 5

for i in range (10,0,-1):
    print(i)
    if i == 5:
        break
print("Out of loop")
    

################################# CONTINUE ########################################

for i in range(1,11):
    if i>5:
        continue
    print(i)
print("Out of loop")


############################### PASS ##########################################

#to display nos from 1 to 10

for i in range(1,11):
    if i >5:
        pass
    print(i)
print("out of loop")

#to display negative nos from a list of given nos

li = [-1,-8,-3,0,3,4]

for i in li:
    if i>=0: #we are not interested in the positive nos
        pass
    else:
        print(i)

################################# ASSERT #########################################
    
x = int(input("Enter a positive no :"))

assert x>0 ,"please enter a positive no"
print("U entered :",x)

#program to handle assertion error that is given by assert statement

x = int(input("Enter a no :"))

try:
    assert(x>0)
    print("U entered :",x)
except AssertionError:
    print("Please enter a positive no.")
    

################################## RETURN ########################################

def add(a,b):
    return a + b

print(add(3,4))
    
#program to display prime nos series

maxi = int(input("Enter a no:"))

for num in range(2,maxi+1): #represents number from 2 to given nos
    for i in range(2,num): #represents number from 2 to i-1
        if (num % i) == 0: #not prime 
            break
    else:
        print(num)


#program to print fibonacci series

n = int(input("Enter a no."))

a = 0
b = 1


for i in range(n):
    print(a)
    c = a + b
    a,b=b,c


################################ SERIES ########################################
    
#program to generate sine value of a given angle in degrees
    
x , n = [int(i) for i in input("Enter the angle and the no. of iterations :").split()]

#converting angle into radians

r = (x*3.14159)/180

#this becomes the first term

t = r

#till now, finding the sum

sum_ = r

#display the iteration nos and the sum

print("Iteration no.{} and the sum {}".format(1,sum_))

#denominator for the second term
i = 2

#iterate through the second term

for j in range(2,n+1):
    t = (-1)*t*r*r/(i*(i+1)) #finding the next term 
    sum_ = sum_ + t
    print("Iteration no.{} and the sum :{}".format(j,sum_))
    i +=2
    
#program for finding the value of the cosine series
    
m,n = [int(i) for i in input("Enter value of degrees and the nos of iterations :").split()]

#converting angle into radians

r = (m*3.14159)/180

#this is the first term'
t= 1

#the sum
sum_ = 1

#printing the value of the first term and the sum
print("no of iterations:{} and sum :{}".format(1,sum_))

#denominator for the second term 
i=1

#iterating through the next term 
for j in range(2,n+1):
    t = (-1)*t*r**2/(i*(i+1))
    sum_ = sum_ + t
    print("Iteration no.{} and the sum :{}".format(j,sum_))
    i +=2
    
#evaluating the exponential series

x , n = map(int,input("Enter power of e and no of iterations :").split())

#first term and the sum
t = 1
sum_ = 1

#printing the first term and the first iteration 

print("No. of iteration:{}  Sum :{}".format(1,sum_))

#iterating 
 
for j in range(1,n):
    t = t * x/j
    sum_ += t
    print("No. of iteration:{}  Sum :{}".format(j+1,sum_))

