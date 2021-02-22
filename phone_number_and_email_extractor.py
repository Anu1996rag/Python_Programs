# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:31:21 2020

@author: Gurudas

PHONE NUMBER AND EMAIL ADDRESS EXTRACTOR
"""
import re,pyperclip

#creating regex for phone numbers - US country 

phoneRegEx = re.compile(r'''(
                        (\d{1,3}|\(\d{1,3}\))?  #area code
                        (\s|-|\.)?          #separator
                        (\d{3})             #first three digits
                        (\s|-|\.)           #separator
                        (\d{4})             #last four digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?   #extension
                        )''',re.VERBOSE)

#creating regex for mail address

emailRegEx = re.compile(r'''(
                             [a-zA-Z0-9._%+-]+      #username
                             @                      #symbol
                             [a-zA-z0-9-+.]+        #domain name
                             (\.[a-zA-Z]{2,4})      #dot something
                             )''',re.VERBOSE)

#finding matches in a clipboard text 

text = str(pyperclip.paste())

matches = []

for groups in phoneRegEx.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != ' ':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegEx.findall(text):
    matches.append(groups[0])

#joining the matches to the string in a clipboard
    
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard...")
    print('\n'.join(matches))
else:
    print('No matches found...!')
    
    
