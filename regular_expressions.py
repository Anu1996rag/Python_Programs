# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:38:53 2020

@author: Gurudas

Regular Expressions
"""
##### Optional matching with the question mark

import re

batRegEx = re.compile(r'bat(wo)?man')

mo1 = batRegEx.search('batman')
print(mo1.group())


mo2 = batRegEx.search('batwoman')
print(mo2.group())

############ GREEDY AND NON-GREEDY MATCHING #################

greedyRegEx = re.compile(r'(ha){3,5}')

mo1 = greedyRegEx.search('hahahahaha')
print(mo1.group())


nonGreedyRegEx = re.compile(r'(ha){3,5}?')

mo2 = nonGreedyRegEx.search('hahahahaha')
print(mo2.group())

################# CHARACTER CLASSES ########################

xmasRegEx = re.compile(r'\d+\s\w+')

xmasRegEx.findall('12 drummers ,10 pipers ,9 ladies')

#finding out vowels from a string 

vowels = re.compile(r'[aeiouAEIOU]')

string = input("Enter a string :")

print(vowels.findall(string))

################ Caret and dollar sign ####################

beginsWith = re.compile(r'^Hello')

mo1 = beginsWith.search('Hello world !')

print(mo1.group())

endsWith = re.compile(r'good$')

mo2 = endsWith.search('If it ends good , it feels good')

print(mo2.group())

exactMatch = re.compile(r'^exact$')

mo3 = exactMatch.search('Exactly , I need the exact data points which we had earlier.')

print(mo3.group())


mo4 = exactMatch.search('exact , I need the exact data points which we had earlier.')

print(mo4.group())


mo5= exactMatch.search('exact')

print(mo5.group())

################## THE WILDCARD CHARACTER #############################

atRegEx = re.compile(r'.at') #this '.' character matches only a single character

print(atRegEx.findall('there\'s a cat on the mat inside a flat.')
      
############# MATCHING EVERYTHING WITH DOT STAR #######################

matchRegEx = re.compile(r'First Name :(.*) , Last Name :(.*)')

mo1 = matchRegEx.search('First Name :Anurag , Last Name :Patil')

print(mo1.group())

nonGreedyRegEx = re.compile(r'<.*?>')

mo = nonGreedyRegEx.search('<TO serve a man> for dinner >')

print("non greedy search :",mo.group())


greedyRegEx = re.compile(r'<.*>')

mo1 = greedyRegEx.search('<TO serve a man> for dinner >')

print("greedy search :",mo1.group())

################### MATCHING NEWLINES WITH DOT CHARACTER ####################

newLineRegEx = re.compile(r'.*')

print(newLineRegEx.search('this is an example.\nof regex without matching new lines.').group())


newLineRegEx = re.compile(r'.*',re.DOTALL)

print(newLineRegEx.search('this is an example.\nof regex with matching new lines.').group())

############### CASE INSENSITIVE MATCHING ####################

caseInsenstiveRegEx = re.compile(r'robo',re.I)

print(caseInsenstiveRegEx.findall('Robo or robo does not matter.It gives all RoBO ,RoBo ,rObO results'))

############### SUBSTITUTING STRINGS WITH THE sub() METHOD ###########

nameRegEx = re.compile(r'Agent \w+')  #this pattern will match only two words one with Agent and second can be any word followed by the word 'Agent'

nameRegEx.sub('Censored','Agent Bob has been informed by Agent Alice')

####

agentNameRegEx = re.compile(r'Agent (\w)\w*')

agentNameRegEx.sub('\1*******','Agent Bob has been informed by Agent Alice')

