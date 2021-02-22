# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:03:03 2020

Functions - Basics

"""

####### Simple Hello Function #########

def hello(name):
    print('Hello '+name)
    
hello('xyz')


####### Magic 8 ball Game ########

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy. Try again.'
    elif answerNumber == 5:
        return 'Ask again later.'
    elif answerNumber == 6: 
        return 'Concentrate and try again'
    elif answerNumber == 7:
        return 'My Reply is no.'
    elif answerNumber == 8:
        return 'Outlook not so good.'
    else:
        return 
    
#r = random.randint(1, 9)
#fortune = getAnswer(r)
print(getAnswer(random.randint(1, 9)))
print(getAnswer(9))


##### LOCAL VARIABELS CANNOT BE USED IN GLOBAL SCOPE ############

def spam():
    eggs = 313375
    
spam()
print(eggs)



####### LOCAL SCOPES CANNOT BE USED IN ANOTHER LOCAL SCOPES ########        

def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham=111
    eggs=0
    
spam()



######## GLOBAL VARIABLES CAN BE READ FROM A LOCAL SCOPE ############

def spam():
    print(eggs)

eggs=42
spam()


######### LOCAL AND GLOBAL VARIABLES WITH THE SAME NAME ############

def spam():
    eggs = 'spam local'
    print(eggs)
    
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
    
eggs = 'global'
bacon()
print(eggs)

####### THE "GLOBAL" STATEMENT #################    

def spam():
    global eggs 
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)


## 2nd program ##

def spam():
    global eggs
    eggs = 'spam' #this is global
    
def bacon():
    eggs='bacon' #this is local
    
def ham():
    print(eggs)#this is global
    
eggs=42 #this is global
spam()
print(eggs) #this is global


################# ASSIGNMENT : COLLATZ SEQUENCE ######################

def collatz(number):
    print(number)
    while (number != 1):
        if (number % 2 ==0):
            number= number // 2
            print(number)
        else:
            number = 3*number+1
            print(number)

try:
    print("Enter a number:")
    user_input = int(input())
    print("***************** Collatz Sequence ******************")
    collatz(user_input)
except:
    print("Enter a valid integer")

