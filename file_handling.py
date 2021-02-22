# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:30:05 2020

@author: Gurudas

File Handling Operations

"""
## Creating new files 

import os

files = ['test_doc.docx','test.csv','test.pptx']

for filename in files:
    print(os.path.join(r'E:\Python\Python Programs',filename))


print(os.path.abspath('.'))

print(os.path.isabs(os.path.abspath('.')))


#to find out the size of the particular directory / size of the all the files in the total

totalSize = 0

for filename in os.listdir(r'E:\Python\Python Programs'):
    totalSize = totalSize + os.path.getsize(os.path.join(r'E:\Python\Python Programs',filename))

print("Total Size(in bytes) :",totalSize)

#########################################################################################

# =============================================================================
# Opening a file using open() function
# =============================================================================

fileOpen = open(r'E:\Python\Python Programs\file_handling.py')


# =============================================================================
# reading the contents of the file using the read() function
# =============================================================================


fileContent = fileOpen.read()
print(fileContent)

fileContent = fileOpen.readlines()
print(fileContent)


# =============================================================================
# writing to files using write() function  in write and append mode
# =============================================================================

baconFile = open('bacon.txt','w') #opening a file in write mode . this will create a new file if it doesn't exists
baconFile.write('Heloooooooo !\n') #writing to the file
baconFile.close() #closing the file 


baconFile = open('bacon.txt','a') #opening a file in append mode
baconFile.write('this is an appended text !\n') #adding contents  to the file
baconFile.close() #closing the file 


baconFile = open('bacon.txt') #opening a file in read mode
fileContent = baconFile.read() #reading  file contents 
baconFile.close() #closing the file 

print ("*********** File Content **************")
print(fileContent)

# =============================================================================
# saving variables with pprint.pformat() function
# =============================================================================

import pprint

cats = [{'name':'Zoey','desc':'chubby'},{'name':'Pika','desc':'fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py','w')
fileObj.write('cats =' + pprint.pformat(cats) + '\n')
fileObj.close()

##importing the myCats file and displaying the variables here

import myCats

print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])