'''
Created on Apr 5, 2013

@author: Cameron Wyatt
'''
"""
Hello, coders! An important part of programming is being able to apply your programs, 
so your challenge for today is to create a calculator application that has use in your life. 
It might be an interest calculator, or it might be something that you can use in the classroom. 
For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!

http://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
"""

def calculate_kinetic_energy():
    mass = raw_input("Enter the mass of the object: ")
    while len(mass) == 0:
        print "Mass cannot be empty"
        mass = raw_input("Enter the mass of the object: ")
    velocity = raw_input("Enter the velocity of the object: ")
    while len(velocity) == 0:
        print "Velocity cannot be empty"
        velocity = raw_input("Enter the velocity of the object: ")
    print str(.5 * float(mass) * float(velocity)**2) + " Newtons"
    
def calculate_potential_energy():
    mass = raw_input("Enter the mass of the object: ")
    while len(mass) == 0:
        print "Mass cannot be empty"
        mass = raw_input("Enter the mass of the object: ")
    height = raw_input("Enter the height of the object: ")
    while len(height) == 0:
        print "Height cannot be empty"
        height = raw_input("Enter the height of the object: ")
    print str(9.8 * float(mass) * float(height)**2) + " Newtons"
    
def get_user_response():
    print "1) Calculate kinetic energy of an object"
    print "2) Calculate potential energy of an object"
    choice = raw_input("Choice: ")
    if choice == "1":
        calculate_kinetic_energy()
    elif choice == "2":
        calculate_potential_energy()
    else:
        print "No valid choice made"
        get_user_response()
        
get_user_response()    
        
 
