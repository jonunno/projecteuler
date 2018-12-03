# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:47:36 2018

Problem 55 from project euler.org

Worked on 
2018/09/30 (solved)

@author: Jon
"""

def is_palin(n):
    # checks if n is a palindrome
    for i in range(0,int(len(str(n))/2)):
        
        if str(n)[i] != str(n)[-(i+1)]:
            return False
        
    return True

def rev_string(n):
    # reverses a string
    result = ''
    for i in range(0,len(str(n))):
        result += str(n)[-(i+1)]
    return result

#count = 9999 # count the number of Lychrel numbers, initially assume all numbers
#    # are Lychrel numbers
    
count = 10000

for i in range(0,10000):
    # test all numbers from 0 up to 9999
    
    num = i
    j = 0
    while j < 50:
        # iterate to try to produce palindrome
        if j > 0 and is_palin(num) == True:
            # num is palindrome, decrease counter and move to next i
            count -= 1
            break
        # Go through one iteration, reverse num and add it to num
        num += int(rev_string(int(num)))
        
        # increment iteration counter
        j += 1
    
print(count)