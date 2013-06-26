'''
Created on Apr 8, 2013

@author: Cameron Wyatt
'''
"""
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!

http://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/"""

from random import randint

def write_to_file(passwords):
    with open("passwords.txt", "w") as my_file:
       for i in range(0, len(passwords)):
            message = ("Password %d is %s") % (i+1, passwords[i])
            my_file.write(message + "\n") 

while True:
    try:
        number_passwords = int(raw_input("How many passwords do you want to generate: "))
        break
    except:
        print "Must be an integer"
        
while True:
    try:
        password_length = int(raw_input("How long should each password be: "))
        break
    except:
        print "Must be an integer"
        
password_count = 0
passwords = []
while password_count < number_passwords:
    temp_password = ''
    length_count = 0
    while length_count < password_length:
        temp_password += (chr(randint(33, 126)))
        length_count+=1
    passwords.append(temp_password)
    password_count+=1

for i in range(0, len(passwords)):
    print ("Password %d is %s") % (i+1, passwords[i])

write_to_file(passwords)    