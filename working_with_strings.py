# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:29:19 2020

@author: Gurudas

Working with strings

"""

# program asking for user to enter his/her age
while True :
    age = input("Enter your age :")
    if age.isdecimal():
        print("Thank you !")
        break
    print("Please enter a number for your age.")
    
#program asking to enter password to user
    
while True:
    password = input("Please enter password :")
    if password.isalnum():
        print("Access Granted !")
        break
    print("Passwords should only have letters and numbers.")

#########################################################################
    
print('hello'.center(20,'*'))

######################################################

def printPicnic(itemsDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for key,value in itemsDict.items():
        print(key.ljust(leftWidth,'.')+str(value).rjust(rightWidth))
        
picnicItems = {'sandwiches':4,'waffles':12,'apples':10,'cups':5,'cookies':7}

printPicnic(picnicItems,15,6)


######################################################################

#copying the contents of the clipboard and pasting using pyperclip module

import pyperclip

pyperclip.copy("Copied to clipboard.....")
pyperclip.paste()


