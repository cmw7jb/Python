'''
Created on May 28, 2013

@author: Cameron Wyatt
'''

"""
Calculates the digital root of a number
    (http://en.wikipedia.org/wiki/Digital_root)
    Using modular arithmetic and string arithmetic (treat the number as
        a string, and sum each digit of that string)
Calculates the persistence, or the number of times the number must be
    summed to be < 10
Times each method over <num_loops> iterations and compares the results
"""

import time
from random import randint


def mod_sum(num):
    """Calculate the digital root using modular arithmetic"""
    num = int(num)
    sum_ = 0
    while num > 0:
        sum_ += num % 10
        num /= 10
    return sum_


def string_sum(num):
    """Calculate the digital root using string arithmetic"""
    str_ = str(num)
    sum_ = 0
    for n in str_:
        sum_ += int(n)
    return sum_


def main():
    """Drive the program"""
    value = randint(1, 1000000)
    num_loops = 10000000

    number = value
    print "Calculating digital root of number {}".format(number)
    start_time = time.clock()
    persistence = 0
    for i in range(num_loops):
        while number >= 10:
            number = mod_sum(number)
            persistence += 1
    end_time = time.clock()
    mod_time = end_time - start_time
    print "Modular arithmetic"
    print "Final number = {}, persistence = {}".format(number, persistence)
    print "Took time {} seconds for {} iterations".format(mod_time, num_loops)

    print

    number = value
    print "Calculating digital root of number {}".format(number)
    start_time = time.clock()
    persistence = 0
    for i in range(num_loops):
        while number >= 10:
            number = string_sum(number)
            persistence += 1
    end_time = time.clock()
    str_time = end_time - start_time
    print "String arithmetic"
    print "Final number = {}, persistence = {}".format(number, persistence)
    print "Took time {} seconds for {} iterations".format(str_time, num_loops)

    differential = mod_time - str_time
    if differential > 0:
        print "String arithmetic won by {} seconds".format(abs(differential))
    else:
        print "Modular arithmetic won by {} seconds".format(differential)


if __name__ == '__main__':
    main()
