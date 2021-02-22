# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 12:36:07 2020

@author: Gurudas

A Short Program : Guess the  number
"""

#this is a small guess the number program

import random 

secretNumber = random.randint(1,20)

print("Am thinking of a number between 1 and 20...")

for guessesTaken in range(7) : #this will make the user to guess 6 times
    print("Take a guess :")
    guess = int(input()) #taking number from the user as a guess
    
    if guess < secretNumber :
        print("Your guess is too low.")
    elif guess > secretNumber :
        print("your guess is too high.")
    else:
        break
    
if guess == secretNumber :
    print("You guessed the correct number in "+str(guessesTaken+1)+" guesses !")
else :
    print("Nope ! The number I was thinking of was",secretNumber)
