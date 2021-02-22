# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:23:57 2020

@author: Gurudas

Strings And Character Operations
"""

#Comparing strings

str1 = "abc2d"

str2 = 'abc2e'

if len(str1) == len(str2):
    print("lengths are equal")

      

if str1==str2:
    print('strings are equivalent')
else:
    print('they are not')
    

##########################finding the sub-string in a given string######################
    
#program to find the first occurrence of a sub-string in a given string 
    
str1 = input("Enter a string :")

sub = input("Enter a substring you want to find:")

n = str1.find(sub,0,len(str1))

# syntax of find function : find(substring , beginning of the string, ending of the string)
# returns -1 if no substring found

if n == -1:
    print("no substring found.")
else:
    print("Substring found at :",n+1)

####################### finding the substring using index()method#####################

str1 = input("Enter a string :")

sub = input("Enter a substring you want to find:")    

try :
    n = str1.index(sub,0,len(str1))
except ValueError:
    print("Sub-string not found.")
else:
    print("Sub-string found at position :",n+1)
 
    
############# FInding all the occurrences of sub-string in a  string ##############
    

str1 = input("Enter a string :")

sub = input("Enter a substring you want to find:") 

n= len(str1)

i=0 #initialization

flag = False

while i < n:
    pos = str1.find(sub,i,n)
    if pos != -1:
        print("Sub-string found at position:",pos+1)
        flag = True
        i = pos+1 # start finding for the next occurrence
    else:
        i +=1 #search from next character onwards
        
if (flag == False):
    print("NO substring found")


######################## Counting substrings in a string #############################

str1 = "Maharashtra"

print(str1.count('a'))

######################## Replacing a string with another string #########################

#version 1

str1 = "this is a wonderful place to live in."

print(str1.replace('wonderful','beautiful'))

#version 2

str2 = 'awesome'

print(str1.replace('wonderful',str2))

#################### Splitting and Joining Strings ###############################

str1 = "this is a wonderful place to live in."

print(str1.split(' '))

sep_list = str1.split(' ')

print(' '.join(sep_list))

##################### CHnaging the case of a string ############################

str1 = "Maharashtra"

#to convert all the characters in upper case

print(str1.upper())

#to convert all the characters in lower case

print(str1.lower())

#to swap the lower case to upper case and upper case to lower case

print(str1.swapcase())

#to print the title case characters

print(str1.title())

##################  checking starting and ending of a string ###################

str1 = 'this a test statement'

#startswith() method checks whether the given string starts with the particular sub string
#returns True or False

print(str1.startswith('this'))

#endswith() method works the similar way as of startswith() method

print(str1.endswith('statement'))

###################### Formatting strings ############################

num = 1000

print('{:*>15d}'.format(num)) #here the number 15 means it will allocate 15 spaces for the number

print('{:*^15d}'.format(num))

#this will print the decimal format value with * marks and the number in the center justified

print('{:*<15d}'.format(num))

#printing hex value 

print('{:*^8x}'.format(num)) 

#printing binary value

print('{:b}'.format(num))

#printing octal values

print('{:o}'.format(num))

####################### Working with Characters ############################

#program to know the type of character entered by user

str1 = input("Enter a character :")

ch = str1[0] #taking only the first input

if ch.isalnum() :#check if it is alphabet or number
    print("It is a alphabet or number")
    if ch.isalpha():
        print("It is an alphabet.")
        if ch.isupper(): #check if it is uppercase letter
            print("it is an uppercase letter.")
        else:
            print("it is lowercase letter")
    else:
        print("It is a number.")
elif ch.isspace():#check if it is a space
    print("it is a space")
else:
    print("It is a special character")
    
    
############################## Sorting Strings ###################################
    
#sorting groups of strings

str1 =[]

#accept how many strings 
n= int(input("Enter no. of strings you want:"))     

for i in range(n):
    print("Enter the string :",end ='')
    str1.append(input())

#sorting the list of strings
str2 = sorted(str1)

print("sorted strings :")
for i in str2:
    print(i)
    
    
    
############################ Finding no. of characters and words in string ##############
    
str1 = "this is a sample statement"

count = 0

for i in str1:
    if i == ' ':
        continue
    count +=1
print("total characters :",count)

#finding no. of words in a string

str1 = "this is a sample statement"

word_count = 0

i = 0

flag = True #becomes False when there is not space

for s in str1:
    if flag == False and str1[i] == ' ' :
        word_count +=1
    #if there's a space
    if str1[i]==' ':
        flag = True
    else:
        flag = False
    
    i+= 1 #fiding for the next word

print("no. of words :",word_count+1)


##################### Inserting a sub-string into a string ######################

str1 = input("Enter a string:")
sub = input("Enter a sub-string you want to enter:")
 
n = int(input("enter position no where you want to enter :"))
 
n = n -1 #decreasing by 1 as the indexing starts from 0
 
str2 = [] #empty list
 
for i in range(n):
     str2.append(str1[i])

#appending the sub-string here
for i in range(len(sub)):
    str2.append(sub[i])
    
#appending the remaining elemnets from str1
for i in range(n,len(str1)):
    str2.append(str1[i])
    
#converting the list elements into string
    
str2 = ''.join(str2)

print(str2)