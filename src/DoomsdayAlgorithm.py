'''
Created on Apr 10, 2013

@author: Cameron
'''
"""This program will take a day, month, and year and determine which day of the week it is

Algorithm:
Find the day of the week the doomsday falls on
    This is the last day of february

Even months
    2nd month, doomsday is the 2nd of the month
    4th month, doomsday is the 4th of the month
    6th month, doomsday is the 6th day of month
    etc

Odd Months
    9-5 at 7-11
    9th month, doomsday is the 5th of the month
    5th month, doomsday is the 9th of the month
    7th month, doomsday is the 11th of the month
    11th month, doomsday is the 7th of the month
    March:
        0th day of march is doomsday
        7th day of match is doomsday
    January:
        January 3rd is doomsday 3/4 times, the non-leap years
        January 4th only on leap year
        

"""

from math import floor

century_doomsday = {"Tuesday" : lambda year : (year % 400) == 0,
                    "Sunday" : lambda year : (year % 400) == 100,
                    "Wednesday" : lambda year : (year % 400) == 300,
                    "Friday" : lambda year : (year % 400) == 200
                    }

days = {"Sunday" : 1, "Monday" : 2, "Tuesday" : 3, "Wednesday" : 4, "Thursday" : 5, "Friday" : 6, "Saturday" : 7}

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif int(year % 4) == 0:
        if int(year % 100) == 0:
            return False
        else:
            return True
    else: 
        return False

def round_to_nearest_century(year):
    return int(floor(year / 100) * 100)    

def get_century_doomsday(year):
    if century_doomsday["Tuesday"](year):
        return "Tuesday"
    elif century_doomsday["Sunday"](year):
        return "Sunday"
    elif century_doomsday["Wednesday"](year):
        return "Wednesday"
    elif century_doomsday["Friday"](year):
        return "Friday"
    else:
        return

def get_year_doomsday(year):
    nearest_century = round_to_nearest_century(year)
    century_doomsday = get_century_doomsday(nearest_century)
    
    decades = year % nearest_century
    
    dividend = int(decades / 12)
    remainder = decades % 12
    final = dividend + remainder + int((remainder / 4))
    while final >= 7:
        final -= 7
    century_doomsday_day = days[century_doomsday]
    if century_doomsday_day + final > 7:
        day_number = century_doomsday_day + final - 7
    else:
        day_number = century_doomsday_day + final
        
    for day, number in days.items():
        if number == day_number:
            day_of_week = day
    return day_of_week

def get_doomsday_of_month(month, year):
    #If month is even, use one rule
    if month == 1:
        if is_leap_year(year):
            month_doomsday = 4
        else:
            month_doomsday = 3
    elif month == 2:
        if is_leap_year(year):
            month_doomsday = 29
        else:
            month_doomsday = 28
    elif month == 3:
        month_doomsday = 7
    elif month == 4:
        month_doomsday = 4
    elif month == 5:
        month_doomsday = 9
    elif month == 6:
        month_doomsday = 6
    elif month == 7:
        month_doomsday = 11
    elif month == 8:
        month_doomsday = 8
    elif month == 9:
        month_doomsday = 5
    elif month == 10:
        month_doomsday = 10
    elif month == 11:
        month_doomsday = 7
    elif month == 12:
        month_doomsday = 12
    else:
        return
    return month_doomsday

def get_day(day_of_month, doomsday_of_month, doomsday_day_of_week_number):
    #day = day of month
    #month = doomsday of month, 4th month - 4, etc
    temp_day = day_of_month - doomsday_of_month
    while temp_day > 7:
        temp_day -= 7
    temp_sum = temp_day + doomsday_of_month
    if temp_sum > 7: 
        temp_sum = 7 - temp_sum
    day_to_check = doomsday_day_of_week_number + temp_sum
    for day, number in days.items():
        if number == day_to_check:
            return day 

def get_input():
    date = raw_input("Enter the date in the format DD/MM/YYYY: ")
    while len(date) == 0:
        print "Date cannot be empty"
        date = raw_input("Enter the date in the format DD/MM/YYYY")
    date.rstrip()
    return (date.split("/"))
    
if __name__ == "__main__":
    parts_of_date = get_input()
    if len(parts_of_date) != 3:
        print "Date incorrectly formatted"
        get_input()
        
    year = int(parts_of_date[2])
    year_doomsday_day_name = get_year_doomsday(year)
    if is_leap_year(year):
        print ("This year is a leap year, the 29th of February (doomsday) is %s") % (year_doomsday_day_name)
    else:
        print ("This year is not a leap year, the 28th of February (doomsday) is %s") % (year_doomsday_day_name)
        
    month = int(parts_of_date[0])
    month_doomsday_day = get_doomsday_of_month(month, year)
    
    year_doomsday_day_number = days.get(year_doomsday_day_name)
    
    day = int(parts_of_date[1])
    
    final_day = get_day(day, month, year_doomsday_day_number)
    print ("Final day is %s") % (final_day) 
    
    
