# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:34:49 2020

@author: Gurudas

Working with lists
"""

############ to add items/elements in the list ###########

cats = [] #empty list

while True: #this will run forever
    print('Enter name of the cat '+ str(len(cats) + 1) +' Or enter nothing to stop.')
    name = input()
    
    if name == '': #blank space
        break #come out of the loop
    
    cats.append(name) #attaching the name to the cats list
    
print("Cats list is:")
for name in cats:
    print(name)
    

