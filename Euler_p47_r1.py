# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:14:14 2018

Problem 47 from project euler.org

Worked on 
2018/11/02 ()

@author: Jon
"""

# check if number is prime
def is_prime(n):
    # return true if n is prime, false otherwise
    if n <= 1:
        return False
    elif n == 2:
        return True
    else: 
        for i in range(2,n):
            # check if all numbers up to but not including n are factors of n
            if n%i == 0:
                return False
        return True
    
# define counter i, which increments by one until n consecutive numbers 

