'''
Created on Apr 4, 2013

@author: Cameron Wyatt
'''
"""create a program that will ask the users name, age, and reddit username. 
have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.

from: http://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/"""

def get_user_name():
    return raw_input("Enter your name: ")

def get_age():
    return raw_input("Enter your age: ")

def get_reddit_username():
    return raw_input("Enter your reddit username: ")

def print_info():
    user_name = get_user_name()
    while len(user_name) == 0:
        print "Name cannot be empty"
        user_name = get_user_name()
    
    age = get_age()
    while len(age) == 0:
        print "Age cannot be empty"
        age = get_age()
        
    reddit_username = get_reddit_username()
    while len(reddit_username) == 0:
        print "Reddit username cannot be empty"
        reddit_username = get_reddit_username()
        
    message = ("Your name is %s, you are %s years old, and your username is %s") % (user_name, age, reddit_username)
    print message
    with open("output.txt", "w") as my_file:
        my_file.write(message)
    
print_info()


