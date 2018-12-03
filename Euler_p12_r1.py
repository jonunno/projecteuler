# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 23:04:20 2018

Problem 12 from project euler.org

Worked on 
2018/09/22 (solution works but takes several hours)

@author: Jon
"""

import numpy

def tri(n):
    # computes the nth triangle number
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# initialize counter to keep track of divisors
num_div = 0

# set a counter to increment through triangle numbers
n = 0

while num_div <= 500:
    
    # increment the counter for triangle numbers
    n += 1
    
    # compute the nth triangle number
    test_tri = tri(n)
    
    # find the divisors of the nth triangle number
    # reset the number of divisor counter
    num_div = 0
    
    for i in range(1,test_tri+1):
        if test_tri%i == 0: # i is a divisor, increment num_div
            num_div += 1
    

    
    