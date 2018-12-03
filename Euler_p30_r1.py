# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 60 from project euler.org

Worked on 
2018/09/26 (solved)

@author: Jon
"""

total = 0 # keep track of the sum of all numbers that fit the problem description

num = 2 # loop through numbers starting at 2

add = 0 # sum of fifth powers of individual digits


while num < 1000000: # there's no good justification for the max value of num
    add = 0 
    
    for i in range(0,len(str(num))):
        add += int(str(num)[i])**5
        
    if add == num:
        total += add
        
    num += 1
    
print(total)