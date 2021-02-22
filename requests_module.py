######################################################################
# Downloading files using requests module
#######################################################################

import requests

res = requests.get('https://www.amazon.in/404 not found')

print(len(res.text))

print(res.__getstate__)

print(res.headers)

print(res.raise_for_status()) #checks for the errors if the page already exists in the website or not

print(requests.codes.ok) # checks if the browser has responded with the status 200 

