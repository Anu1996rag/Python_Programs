# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:25:30 2020

@author: Gurudas

Exception Handling
"""

### Simple Zero Division error program ###

def divideby(number):
    try :
        return 42.0/number
    except ZeroDivisionError:
        print("invalid argument.")

print(divideby(12))
print(divideby(2))
print(divideby(0))
print(divideby(1))

### Simple Zero Division error program - MOdified###

def divideby(number):
    return 42/number

try:
    print(divideby(12))
    print(divideby(2))
    print(divideby(0))
    print(divideby(1))
except ZeroDivisionError:
    print('invalid argument')
