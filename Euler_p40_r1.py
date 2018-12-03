# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:01:38 2018

Problem 40 from project euler.org

Worked on 
2018/09/30 (solved)

@author: Jon
"""

# concatenate positive integers

constant = ''

i = 1
while len(constant) < 1000000:
    # add i to the end of constant and increment i
    constant += str(i)
    i += 1
    
print(len(constant))

prod = 1 # find the product of the requested dn
for i in range(0,7):
    prod *= int(constant[10**i-1])
    print(constant[10**i-1])
    
print(prod)
    