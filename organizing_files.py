# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:22:01 2020

@author: Gurudas

Organizing files
"""

import shutil

# =============================================================================
# copying files and folders
# =============================================================================

shutil.copy(r'E:\Python\Python Programs\bacon.txt',r'E:\Python')

#copying the whole folder along with its sub-folders and files in it.

shutil.copytree(r'E:\Python\Python Programs', r'E:\Python\test')

# =============================================================================
# listing all the contents of the folders , sub-folders and files
# =============================================================================

import os 

for folder,subfolders, filenames in os.walk(r'E:\Python\Python Programs'):
    print('The current folder is :',folder)
    
    for subfolder in subfolders:
        print("Present sub-folder is :",subfolder)
    
    for file in filenames:
        print("Present files are :",file)
    
    print(' ')
    
# =============================================================================
# reading the contents from the zip files 
# =============================================================================

import zipfile

exampleZip = zipfile.ZipFile(r'E:\Data Science\Zip files\S28_L149.zip')

exampleZip.namelist()

sampleInfo = exampleZip.getinfo('1.02. Multiple linear regression.csv')

#Actual file size
print(sampleInfo.file_size)

#compressed size
print(sampleInfo.compress_size)


print("Compressed size is %sx smaller than actual file size"%round((sampleInfo.file_size/sampleInfo.compress_size),2))

#closing the zipfileObject

exampleZip.close()