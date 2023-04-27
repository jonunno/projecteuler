# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:19:11 2018

Problem 48 from project euler.org

Worked on 
2018/09/24 (solved)

@author: Jon
"""

# initialize a variable to store the sum of the series
sum = 0

for i in range(1,1001):
    
    sum += i**i
    
print(str(sum))