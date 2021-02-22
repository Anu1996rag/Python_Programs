# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 19:09:30 2019

@author: Gurudas

Command Line Arguments 
"""

import sys #most important library to import if you are working with commmand line arguments

n = len(sys.argv) #no. of arguments passed 

args = sys.argv #list of arguments passed

print("No. of arguments passed :",n)

print("List of arguments passed :",args)

print("Each argument one by one :")
for a in args:
    print(a)
    
#to accept the input as the arguments and calculate the sum
    
a = int(sys.argv[1]) #the 0th argument is always the name of the program
b = float(sys.argv[2]) #converting to float

print("Result :",a+b) 