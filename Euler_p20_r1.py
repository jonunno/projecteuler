# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:17:37 2018

Problem 20 from project euler.org

Worked on 
2018/09/23 (solved)

@author: Jon
"""

# calculate 100!
prod = 1

for i in range(1,100+1):
    
    prod *= i
    
print(prod)

# calculate sum of digits in prod
sum = 0

for i in range(0,len(str(prod))):
    
    sum += int(str(prod)[i])
    
print(sum)