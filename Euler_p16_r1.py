# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:12:01 2018

Problem 16 from project euler.org

Worked on 
2018/09/23 (solved)

@author: Jon
"""

# computer 2**1000
prod = 2**1000
print(len(str(prod)))

# compute sum of digits in 2**1000
sum = 0
for i in range(0,len(str(prod))):
    sum += int(str(prod)[i])
    
print(sum)



