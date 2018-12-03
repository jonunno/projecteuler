# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 19 from project euler.org

Worked on 
2018/09/28 (solved)

@author: Jon
"""
# as a convention, say Sunday is 7 and count up from 1 to 7 to represent the days of the week
#   (eg. monday has a value of 1)

# Jan 31
# Feb 28/29
# Mar 31
# Apr 30
# May 31
# Jun 30
# Jul 31
# Aug 31
# Sep 30
# Oct 31
# Nov 30
# Dec 31

count = 0 # count the number of sundays that fall on the first month

def add_day(day, month):
    # takes the initial value, day, and adds the modulus of the length of the 
    # month divided by 7 to find the day at the beginning of the next month
    
    day += month%7

    if day > 7:
        day -= 7
    
    return day


# find the starting day on 1 Jan 1901
day = 1 + (365+1-1)%7 # start 1 Jan 1900 and add 365 days for the year + 1 for leap year - 1 for overlap

if day > 7:
    day -= 7
    



for i in range(1901,2001):
    # increment i to cycle through years
    
    for j in [31,28,31,30,31,30,31,31,30,31,30,31]:
        
        if day%7 == 0:
            count += 1
        
        if j == 28 and (i%4 == 0 and i%400 != 0):
            j = 29
        
        day = add_day(day,j)
        
     
print(count)





