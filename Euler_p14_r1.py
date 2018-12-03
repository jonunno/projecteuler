# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:17:37 2018

Problem 14 from project euler.org

Worked on 
2018/09/24 (solved but takes a few minutes)

@author: Jon
"""

# create function to apply rules
def rule(n):
    if n%2 == 0:
        # n is even
        n /= 2
    else:
        # n is odd
        n *= 3
        n += 1
        
    return n

# create variables to store the largest chainlength and the corresponding number
max_num = 0
max_chain = 0

for i in range(1,1000000):
    chain = 1
    n = rule(i)
    
    while rule(n) > 1:
        chain += 1
        n = rule(n)
        
    if chain > max_chain:
        max_chain = chain
        max_num = i
    
    print(i)
