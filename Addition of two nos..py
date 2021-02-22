# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:34:51 2019

@author: Gurudas
"""

#program to add two nos.

a = 10
b = 20

c = a + b

print("Addition of two nos. a and b is",c)

#using user input

a = input("Enter first no :")
b = input("Enter second no :")

print("Addition of {} and {} is {}".format(a,b,int(a+b)))


#fibonacci nos.

n = int(input("enter the length of the series : "))

a = 0
b = 1 

for i in range(n):
    print(a)
    #print(b)
    c = a + b
   # print(c)
    a = b
    b = c
    
# Check Armstrong number of n digits
    
num = int(input("Enter a no. :"))

order = len(str(num))

sum_ = 0
temp = num 

while temp > 0:
    d = temp % 10
    sum_ = sum_ + d**order
    temp = temp // 10

if (num == sum_) :
    print("It is an armstrong number")
else:
    print("It is not an armstrong number.")
    

#Python program to check if a number is prime:
    
n = int(input("Enter a no.:"))

for i in range(2,n//2):
    if (n%i==0):
        print("It is not a prime no")
        break
    else:
        print("It is a prime no.")
        break

## Python program to display all the prime numbers within an interval
        
upper = int(input("Enter upper no. :"))
lower = int(input("Enter lower no. :"))

for num in range(lower , upper + 1):
    if num >1 :
    #all prime nos are greater than 1
        for i in range(2 , num):
            if (num % i) ==0:
            #print("It is not prime")
                break 
        else: #out of the second for loop
            #print("It is prime")
            print(num)
            
   




