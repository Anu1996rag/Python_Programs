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
            
#to find a factorial of a given no.
            
n = int(input("Enter a no :"))

fact = 1

if n == 0 :
    print(fact)
else :
    for i in range(1,n+1):
        fact = fact * i
print(fact)



#program to find a strong number

#Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number.

def factorial(n):
    fact = 1
    
    if n ==0 or n==1 :
        return fact
    else :
        for i in range(1,n + 1):
            fact = fact * i
        return fact

sum_ = 0 

num = int(input("Enter a no> :"))

temp = num

while temp > 0:
    d = temp % 10
    sum_ = sum_ + factorial(d)
    temp = temp // 10

if sum_ == num :
    print("IT is a strong number")
else :
    print("It is not a strong number")
    
    
#python program to accept a number in any form and convert it into decimal form 
    
str = input("Enter a hexadecimal no :")

n = int(str,16) #number 16 shows that the number has base 16 i.e. hexadecimal no
print("Decimal no for the given hexa no. is",n)


str = input("Enter a octal no :")

n = int(str,8) #number 8 shows that the number has base 8 i.e. octal no
print("Decimal no for the given octal no. is",n)


str = input("Enter a binary no :")

n = int(str,2) #number 2 shows that the number has base 2 i.e. binary no
print("Decimal no for the given binary no. is",n)


#to accept more than one input in a same line

a,b = [ int(x) for x in input("Enter any two nos: ").split()]
print(a,b,end="\n")

#accepting three nos separated by space and summing them 

a,b,c = [int(x) for x in input("Enter three nos. :").split()]
print("Sum of the above three nos :",a+b+c)



#######################usage of eval() function######################################

a,b = 10,4
result = eval("a+b-4")
print(result)

#evaluating an expression entered from keyboard using the input() function

x = eval(input("Enter your expression:"))
print("Result :",x)

#accepting a list from keyboard

x = eval(input("Enter a list :"))
print("List :",x)




