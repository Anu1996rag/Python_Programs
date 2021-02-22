# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:31:48 2020

@author: Gurudas

Web Scraping 
"""

# =============================================================================
# Saving downloaded files to the hard drive
# =============================================================================

import requests

#browsing to the URL

res = requests.get('https://www.amazon.in')

#checking for error
res.raise_for_status()

#creating a new file with the write binary mode

writeFile = open('Amazon_content.txt','wb') #write binary mode is used for handling the unicode data from the browser

#writing the bytes into the file 
for chunk in res.iter_content(10000000):
    writeFile.write(chunk)

#closing the file
writeFile.close()

# =============================================================================
# Parsing the HTML pages with the beautifulSoup module
# =============================================================================

import requests,bs4

res = requests.get('https://www.amazon.in')

#check for error 
res.raise_for_status()

#passing the Response object to beautiful Soup
amazonSoup = bs4.BeautifulSoup(res.text)

#pulling out all the p (paragraph elements) from the page
pElements = amazonSoup.select('p')


str(pElements[0])
pElements[0].attrs['class'][0]


# =============================================================================
# Taking the input as command line arguments and searching in the browser 
#along with first 5 links opening in new tabs
# =============================================================================

import requests,bs4,webbrowser

print('Googling...')
res = requests.get('https://www.google.com/search?q='+'python')

#check for error
res.raise_for_status()

#parsing the downloaded page using beautiful soup
soup = bs4.BeautifulSoup(res.text)

#finding all the hyperlinks from the search result
linkElements = soup.findAll('.r a')

#opening web browser for each result minimum 5
numOpen = min(5,len(linkElements))
for eachLink in range(numOpen):
    webbrowser.open('https://google.com/'+ linkElements[eachLink].get('href'))
    

# =============================================================================
# Downloading the comic images from a website
# =============================================================================


# =============================================================================
# step 1: designing the program
# =============================================================================

import requests,os,bs4

url = 'http://xkcd.com'

#create a new folder 
os.makedirs('xkcd',exist_ok=True)

#loop until the URL ends with '#' sign
while not url.endswith('#'):
    print("Downloading page ... %s" %url)
    res = requests.get(url)
    
    #check for error
    res.raise_for_status()
    
#Step 2 : Downloading the web page
    
    #parsing pages into beautifulSoup
    soup = bs4.BeautifulSoup(res.text)

#Step 3 : Finding and downloading the image file     

    #finding out the URL of the comic image
    comicImage = soup.select('#image img')
    
    if comicImage == []:
        print('Image file not found.')
    else:
        comicUrl = 'http:' + comicImage[0].get('src')
        
        #downloading the image 
        print('Downloading image... %s' %(comicUrl))
        
        res = requests.get(comicUrl)
        
        #check for error 
        res.raise_for_status()
        
#Step 4 : Saving the image and finding the previous comic
        
        #saving the image 
        
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(1000000000):
            imageFile.write(chunk)
        
        #closing the file
        imageFile.close()
        
#Step 5: Getting the previous button URL
    prevLink = soup.select("a[rel='prev']")[0] #selecting the first link 
    url = 'http://xkcd.com' + prevLink.get('href')
        
        
    
    
print('Done.')