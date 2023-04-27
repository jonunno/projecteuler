# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 28 from project euler.org

Worked on 
2018/09/28 (solved)

@author: Jon
"""


total = 1 # starting value at the center of the square
init = 3 # initial value of lower right corner, to pass to calc_corners function


def calc_corners(dim,n):
    # dim is the dimension of the square
    # is the value on the bottom right corner of the square
    
    total = n
    
    for i in range(1,4):
        
        total += n + (dim-1)*i
    
    return [total, n + (dim-1)*i]


for i in range(3,1002,2): # i represents the dimension of each square, increases by 2 
    
    result = calc_corners(i,init) # calculate sum of corners for a square with dimensions i 
    total += result[0] # add sum of corners to total
    init = result[1] + (i + 1) # increase initial value of lower right corner to match sequence
    
print(total)