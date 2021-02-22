# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:02:09 2020

@author: Gurudas

Debugging techniques
"""

# =============================================================================
# Raising Exceptions 
# =============================================================================

def boxPrint(symbol,width,height):
    if len(symbol)!=1:
        #raising exceptions through "raise" keyword
        raise Exception('Symbol must be a single character string...')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
        
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ')*(width - 2) + symbol)
    print(symbol * width)
    
for sym ,w , h in (('*',4,4),('0',20,5),('x',5,6),('$',2,2)):
    try :
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception occurred :' + str(err))
    
        
# =============================================================================
# Assertions 
#    1. the "Assert" keyword.
#    2. the condition
#    3. the comma (,)
#    4. string to display when the condition evaluates to False
# =============================================================================

number = 8

assert number == 7 , "Number should be 7."


#### Traffic light simulations

market_2nd = {'ns':'green','ew':'red'}
mission_16th = {'ns':'yellow','ew':'green'}

def switchLights(stopLight):
    for key in stopLight.keys():
        #including assertion statement for detecting the red values
        assert 'red' in stopLight.values(),'Neither of the lights are red !!!'
        if stopLight[key]=='green':
            stopLight[key]='yellow'
        elif stopLight[key] == 'yellow':
            stopLight[key]= 'red'
        elif stopLight[key] == 'red' :
            stopLight[key] = 'green'
            
switchLights(mission_16th)

#after calling function
print(market_2nd)


# =============================================================================
# Practice Project :  Debugging coint toss
# =============================================================================

import random

guess = ''

while guess not in ('heads','tails'):
    print('Guess the coin toss.. Enter "heads" or "tails":')
    guess = input()
    
    toss = random.randint(0,1) # 0 for tails ,1 for heads 
    
    if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
        print('You got it ..')
    else:
        print('Nope.. ! Try Again :')
        guess = input()
        if (toss == 0 and guess == 'tails') or (toss == 1 and guess == 'heads'):
            print('You got it.')
        else: 
            print('you suck at this..')


