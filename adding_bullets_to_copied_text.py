"""this program is to copy the text to the clipboard and add bullets and spaces at the 
   beginning of each line """

import pyperclip

#taking the text copied to a variable 
text = pyperclip.paste()

#converting the copied text to a list of strings / new lines
lines = text.split('\n')

#looping through each line
for line in range(len(lines)):
    lines[line] = '* ' + lines[line] #rhis adds * and a space to the beginnig of each line

#joining the returned list of strings from the above statement
text = '\n'.join(lines)

pyperclip.copy(text)


