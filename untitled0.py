# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:21:32 2020

@author: Gurudas
"""

from bs4 import BeautifulSoup
import requests 

# =============================================================================
# opening the page 
# =============================================================================

try :
    url = requests.get("https://www.failory.com/blog/top-indian-startups")
    soup = BeautifulSoup(url.text,features='lxml')
except :
    print("Page not found...")

print(soup.prettify())
    
    

