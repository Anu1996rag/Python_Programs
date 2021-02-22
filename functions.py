# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:01:32 2020

@author: Gurudas

Functions
"""

## A function that accepts two values and find their sum

def add(a,b):
    """ This function adds any two nos"""
    c = a + b
    print("Sum =",c)

add(2,3) #calling the function
add(3.5,7.8) #calling the function with different arguments 

#################### RETURNING RESULTS FROM A FUNCTION ############################

##Function to add two nos and the return the result from the function

def add(a,b):
    c = a + b
    return c   #returns the result

#calling the functions

x = add(2,3) #calling the function and storing the result in the x variable
print("Sum =",x)


y = add(2.6,3.5) #calling the function and storing the result in the x variable
print("Sum =",y)


#function to test whether the given number is even or odd

def even_odd(num):
    if num % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
        
even_odd(6) #calling the function

#program to find the factorial of a number

def fact(num):  
    """this is a recursive function to find the factorial of a number"""
    if (num==0) or (num==1):
        return 1
    else:
        return num*fact(num-1)

# to display the factorials of numbers 1 to 10
#calling the function as fact(num)
for i in range(1,11):
    print("Factorial of {} is {}".format(i,fact(i)))
    
### Function to check whether a given number is prime or not
    
def is_prime(num):
    flag = 1 #will become 0 if the number is not prime
    
    for i in range(2,num):
        if (num % i) == 0:
            flag = 0 # if the number is divisible by any number other than 1 or itself
            break
        else:
            flag =1
    return flag

n = int(input("Enter a number :")) #taking input from user

#calling the function

x = is_prime(n)

if x ==1 : #if the returned value is 1
    print("Number is prime")
else:
    print("Number is not prime")

#program to generate prime numbers

def prime(num):
    flag = 1 #will become 0 if the number is not prime
    
    for i in range(2,num):
        if (num % i) == 0:
            flag = 0 # if the number is divisible by any number other than 1 or itself
            break
        else:
            flag =1
    return flag

#generating prime numbers

n = int(input("How many prime nos. you want to be displayed ?  "))

i = 2 #value of i starts with 2
c = 1 #this to count the number of primes

while True : # repeat forever
    if prime(i): #calling the function and if it is true or value is 1
        print(i) #print the number
        c +=1 #increment the count 
    i +=1 #increment the number by 1
    if c > n: #if the count exceeds the given number
        break #break the loop

    
    


        
        