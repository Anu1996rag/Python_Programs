# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:41:53 2020

@author: Gurudas

Nested Dictionaries

"""

allGuests = {
             'Alice':{'apples':5,'pretzels':10},
             'Bob':{'sandwiches':3,'apples':2},
             'Carol':{'cups':5,'apple pies':3}
             }

def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
        print(k) #keys
        print(v) #values of the respective keys
    return numBrought

print("NUmber of things being brought :")
print('--Apples      '+str(totalBrought(allGuests,'apples')))
print('--Cups        '+str(totalBrought(allGuests,'cups')))
print('--Sandwiches  '+str(totalBrought(allGuests,'sandwiches')))
print('--Cup Cakes   '+str(totalBrought(allGuests,'cup cakes')))

###################################################################################

#Inventory

stuff = {'rope':1,'torch':6,'gold coin':42,'arrow':12}

def displayInventory(inventory):
    print("*************Inventory*************")
    totalItems = 0
    for k,v in inventory.items():
        totalItems += int(v)
        #print(k)
        #print(v)
    return totalItems   
displayInventory(stuff)


##################################################################################

##LIST TO DICTIONARY FUNCTION 


dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

def addToInventory(inventory,addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item,0)+1
        
def displayInventory(inventory):
    for key,value in inventory.items():
        print(str(value) + ': '+ key)
        
        
        
inv = {'gold coin':42,'rope':1}

addToInventory(inv,dragonLoot)
displayInventory(inv)
        