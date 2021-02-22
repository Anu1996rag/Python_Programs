#shebang line
#! python3    

#An insecure password locker program

#Dictionary of stored passwords

PASSWORDS = {'email':'fw34f8rvj3024erjv',
             'blog':'f34revji3rveodrgj',
             'luggage':'12345'}

#Actual logic starts here

import sys,pyperclip

if len(sys.argv) < 2 :
    print('Usage :python password_locker.py [account] - copies account password if exists in the locker...')
    sys.exit()

account = sys.argv[1] #first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for "+ account + " has been copied...")
else:
    print("No password for "+ account +" exists in the locker.")

if account not in PASSWORDS:
    print("You want to add in the locker ?(y/n)")
    reply = input()
    if reply == 'y' or reply == 'Y':
        print("Enter password for "+account)
        new_entry = input()
        PASSWORDS[account] = new_entry
        print("Passsword locker manager updated...!")
        print(PASSWORDS)
    else:
        print("Thank you !")
        




             