# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:12:32 2020

@author: Gurudas

Strong password detection
"""

import re

def isStrong(text):
    pattern = re.compile(r'[a-zA-z]+\d{1,}')
    
    if len(text) >= 8 and pattern.search(text):
        return True

password = input("Enter a new password :")

if isStrong(password):
    print("Password accepted ..!")
else:
    print("Enter a strong password with at least 8 characters and at least 1 digit.")
    