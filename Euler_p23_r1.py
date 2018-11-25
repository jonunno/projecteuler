# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:33:13 2018

@author: Jon

ProjectEuler.net

Problem 23

---
Progress
    2018-11-24 (Solved but solution took about 30 minutes)
    
"""

import math


def find_divisors(num):
    """ Returns a set of divisors of num """
    divisors = []
    
    for possible_divisor in range(1,math.ceil((num+1)/2)):
        # try all possible divisors of num (between 1 and num/2 rounded up)
        if num%possible_divisor == 0:
            divisors.append(possible_divisor)
            if possible_divisor != 1:
                divisors.append(int(num/possible_divisor))

    # get unique divisors
    return set(divisors)
        
    
def set_sum(nums):
    """ calculates the sum of numbers in num """
    total = 0
    
    # loop through contents of the set nums and each to the total
    for num in nums:
        total += num
        
    return total
        

def is_abundant(num):
    """ checks if num is abundant """
    if num < set_sum(find_divisors(num)):
        return True
    else:
        return False

# create a list of abundant numbers
abundants = []
for num in range(1,28123+1):
    if is_abundant(num) == True:
        abundants.append(num)
    else:
        pass

# calculate the total of all positive integers that are not the sum of two 
# abundant numbers
total = 0
for num in range(1,28123+1):
    for abundant in abundants:
        if num-abundant < 0:
            total += num
            break
        elif is_abundant(num-abundant) == True:
            break
    
print(total)











