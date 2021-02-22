######################################################################
# Creating a small program that will search for an address 
# in the google maps 
######################################################################

import webbrowser,sys,pyperclip

if len(sys.argv)>1: #check for the command line argument if given
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() #check for the copied content in the clipboard

webbrowser.open('https://www.google.com/maps/place/'+address)

